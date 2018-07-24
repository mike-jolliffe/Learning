// SERVICES
weatherApp.service('cityService', function() {

    this.city = "New York, US";

});

weatherApp.service('weatherService', ['$resource', function($resource) {

    this.GetWeather = function(city, days) {
        var weatherAPI = $resource("https://api.openweathermap.org/data/2.5/forecast?APPID=68dffd555fd13522b27b7fb27f222497", {
        callback: "JSON_CALLBACK"}, { get: { method: "JSONP"}});

        return weatherAPI.get({ q: city, cnt: days });
    }


}]);