var key;
var resp;

var weather_conditions_obj = {
            '200': ['thunderstorm with light rain', 'thunder'],
            '201': ['thunderstorm with rain', 'thunder'],
            '202': ['thunderstorm with heavy rain', 'thunder'],
            '210': ['light thunderstorm', 'thunder'],
            '211': ['thunderstorm', 'thunder'],
            '212': ['heavy thunderstorm', 'thunder'],
            '221': ['ragged thunderstorm', 'thunder'],
            '230': ['thunderstorm with light drizzle', 'thunder'],
            '231': ['thunderstorm with drizzle', 'thunder'],
            '232': ['thunderstorm with heavy drizzle', 'thunder'],
            '300': ['light intensity drizzle', 'rain'],
            '301': ['drizzle', 'rain'],
            '302': ['heavy intensity drizzle', 'rain'],
            '310': ['light intensity drizzle rain', 'rain'],
            '311': ['drizzle rain', 'rain'],
            '312': ['heavy intensity drizzle rain', 'rain'],
            '313': ['shower rain and drizzle', 'rain'],
            '314': ['heavy shower rain and drizzle', 'rain'],
            '321': ['shower drizzle', 'rain'],
            '500': ['light rain', 'rain'],
            '501': ['moderate rain', 'rain'],
            '502': ['heavy intensity rain', 'rain'],
            '503': ['very heavy rain', 'rain'],
            '504': ['extreme rain', 'rain'],
            '511': ['freezing rain', 'rain'],
            '520': ['light intensity shower rain', 'rain'],
            '521': ['shower rain', 'rain'],
            '522': ['heavy intensity shower rain', 'rain'],
            '531': ['ragged shower rain', 'rain'],
            '600': ['light snow', 'snow'],
            '601': ['snow', 'snow'],
            '602': ['heavy snow', 'snow'],
            '611': ['sleet', 'snow'],
            '612': ['shower sleet', 'snow'],
            '615': ['light rain and snow', 'snow'],
            '616': ['rain and snow', 'snow'],
            '620': ['light shower snow', 'snow'],
            '621': ['shower snow', 'snow'],
            '622': ['heavy shower snow', 'snow'],
            '701': ['mist', 'misty'],
            '711': ['smoke', 'misty'],
            '721': ['haze', 'misty'],
            '731': ['sand, dust whirls', 'misty'],
            '741': ['fog', 'misty'],
            '751': ['sand', 'misty'],
            '761': ['dust', 'misty'],
            '762': ['volcanic ash', 'misty'],
            '771': ['squalls', 'misty'],
            '781': ['tornado', 'misty'],
            '800': ['clear sky', 'clear'],
            '801': ['few clouds', 'clouds'],
            '802': ['scattered clouds', 'clouds'],
            '803': ['broken clouds', 'clouds'],
            '804': ['overcast clouds', 'clouds'],
            '900': ['tornado', 'tornado'],
            '901': ['tropical storm', 'storm'],
            '902': ['hurricane', 'storm'],
            '903': ['cold', 'snow'],
            '904': ['hot', 'clear'],
            '905': ['windy', 'wind'],
            '906': ['hail', 'snow'],
            '951': ['calm', 'clear'],
            '952': ['light breeze', 'wind'],
            '953': ['gentle breeze', 'wind'],
            '954': ['moderate breeze', 'wind'],
            '955': ['fresh breeze', 'wind'],
            '956': ['strong breeze', 'wind'],
            '957': ['high wind, near gale', 'wind'],
            '958': ['gale', 'wind'],
            '959': ['severe gale', 'wind'],
            '960': ['storm', 'storm'],
            '961': ['violent storm', 'storm'],
            '962': ['hurricane', 'storm']
};

// Hide API key
function getKey() {
    $.ajax({
        type: "GET",
        url: "key.txt",
        success: function(result) {
            key = result;
        }
    })
}

getKey();

// Gets current lat/long coords
var options = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0
};

function displayWeather(result) {
    resp = parseResponse(result);
            $('#location').html(resp.name);
            $('#description').html("Currently: " + resp.description);
            $('#temp').html(parseInt(resp.temp) + ' &#176;');
            $('#humidity').html(resp.humidity + ' %');
            $('#clouds').html(resp.clouds + ' %');
            changeBackground(resp.condition_code);
}

// Make ajax request after getting current position
function geoSuccess(pos) {
    var crd = pos.coords;

    $.ajax({
        type: "GET",
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            APPID: key,
            lat: crd.latitude,
            lon: crd.longitude,
            units: 'imperial'
        },
        success: displayWeather
    });
}

function geoError(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

// Parse the ajax response into an object
function parseResponse(resp_data) {
    var resp_obj = {
                    'name':resp_data.name,
                    'temp': resp_data.main.temp,
                    'humidity': resp_data.main.humidity,
                    'clouds': resp_data.clouds.all,
                    'description': resp_data.weather['0'].description,
                    'condition_code': resp_data.weather['0'].id,
                    'wind_spd': resp_data.wind.speed,
                    'winddeg': resp_data.wind.deg
    };

    console.log(resp_obj);
    return resp_obj
}

// Change the website background based on current weather conditions
function changeBackground(code) {
    var img_path = 'img/' + weather_conditions_obj[code][1] + '.jpg';
    $('body').css({
                    'background-image': "url(" + img_path + ")",
                    'background-size': 'cover'
    })
}

// Make ajax request based on city entered by user instead of current location
$('#formSubmit').click(function () {
    var city = $('#formCity').val();
    $.ajax({
        type: "GET",
        url: "http://api.openweathermap.org/data/2.5/weather" ,
        data: {
            APPID: key,
            q: city,
            units: 'imperial'
        },
        success: displayWeather
    });
});

// Get current location and run app
navigator.geolocation.getCurrentPosition(geoSuccess, geoError, options);

// Track the toggle for C/F conversion, and convert temperature based on status
$('.switch-input').change(function () {
        if ($('.switch-input').prop('checked') == true) {
            var degC = parseInt((resp.temp - 32) * (5 / 9));
            $('#temp').html(degC + ' &#176;');
        } else {
            var degF = parseInt($('#temp').html().split(" ")[0] * (9/5) + 32);
            $('#temp').html(degF + ' &#176;')
        }
});
