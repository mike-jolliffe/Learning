const request = require('request');
const app_configs = require('../configs');
const API_KEY = app_configs.API_KEY;
const LAT = 45.677;
const LNG = -115.445;


var getWeather = (lat, lng, callback) => {
  request({
    url: `https://api.darksky.net/forecast/${API_KEY}/${lat},${lng}`,
    json: true
  },(error, response, body) => {
    if (!error && response.statusCode === 200) {
      callback(undefined, {
        temperature: body.currently.temperature,
        apparentTemperature: body.currently.apparentTemperature
      });
    } else {
      callback('Unable to fetch weather data.');
    }
  });
};

module.exports.getWeather = getWeather;
