// Gets current lat/long coords
var options = {
  enableHighAccuracy: false,
  timeout: 5000,
  maximumAge: 0
};

function geoSuccess(pos) {
    var crd = pos.coords;

    $.ajax({
        type: "GET",
        url: "http://api.openweathermap.org/data/2.5/weather",
        data: {
            APPID: '0a782a90c9c00349d94ab5ca05d3679c',
            lat: crd.latitude,
            lon: crd.longitude,
            units: 'imperial'
        },
        success: function (result) {
            console.log(result)
            parseResponse(result);
        }
    });
}

function geoError(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

navigator.geolocation.getCurrentPosition(geoSuccess, geoError, options);

function parseResponse(resp_data) {
    var resp_obj = {
                    'temp': resp_data.main.temp,
                    'humidity': resp_data.main.humidity,
                    'clouds': resp_data.clouds.all,
                    'description': resp_data.weather['0'].description,
                    'wind': resp_data.wind.speed,
                    'winddeg': resp_data.wind.deg

    };

    console.log(resp_obj)
}


// Create function that sends an ajax POST request to open weather using city, state
// Grab google images for different conditions
// Parse AJAX response
// Put parsed data into HTML