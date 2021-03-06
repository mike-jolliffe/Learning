var request = require('request');

var geocodeAddress = (address) => {
  return new Promise((resolve, reject) => {
    // Put in request functionality
    var encAddress = encodeURIComponent(address);

    request({
      url: `https://maps.googleapis.com/maps/api/geocode/json?address=${encAddress}`,
      json: true
    },(error, response, body) => {
      if (error) {
        reject('Unable to connect to Google servers.');
      } else if (body.status === 'ZERO_RESULTS') {
        reject('Unable to find that address.');
      } else if (body.status === 'OK') {
        resolve({
          address: body.results[0].formatted_address,
          latitude: body.results[0].geometry.location.lat,
          longitude: body.results[0].geometry.location.lng
        })
      }
    });
  });
}

geocodeAddress('19146').then((location) => {
  console.log(location);
}, (errorMessage) => {
  console.log(errorMessage);
});
