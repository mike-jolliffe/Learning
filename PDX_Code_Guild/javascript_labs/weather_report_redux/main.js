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
            console.log(result);
        }
    });
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

navigator.geolocation.getCurrentPosition(geoSuccess, error, options);

// Create function that sends an ajax GET request to open weather maps API using current lat/long coords


// Create funciton that sends an ajax POST rewquest to open weather using city, state
// Parse AJAX response
// Put parsed data into HTML