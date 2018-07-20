// MODULE
var weatherApp = angular.module('weatherApp', ['ngRoute', 'ngResource']);

// ROUTES
weatherApp.config(function($routeProvider) {
   $routeProvider

       .when('/', {
           templateUrl: 'pages/home.htm',
           controller: 'homeController'
       })

        .when('/forecast', {
           templateUrl: 'pages/forecast.htm',
           controller: 'forecastController'
       })
});

// SERVICES
weatherApp.service('cityService', function() {

    this.city = "New York, US";

});

// CONTROLLERS
weatherApp.controller('homeController', ['$scope', 'cityService', function($scope, cityService) {

    $scope.city = cityService.city;
    $scope.$watch('city', function() {
        cityService.city = $scope.city;
    });


}]);

weatherApp.controller('forecastController', ['$scope', '$resource', 'cityService', function($scope, $resource, cityService) {

    $scope.city = cityService.city;

    $scope.weatherAPI = $resource("https://api.openweathermap.org/data/2.5/forecast?APPID=68dffd555fd13522b27b7fb27f222497", {
        callback: "JSON_CALLBACK"}, { get: { method: "JSONP"}});

    console.log($scope.weatherAPI);
    $scope.weatherResult = $scope.weatherAPI.get({ q: $scope.city, cnt: 2});

    console.log($scope.weatherResult);

}]);