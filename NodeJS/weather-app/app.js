// const yargs = require('yargs');
// const geocode = require('./geocode/geocode');
//
// const argv = yargs
//   .options({
//     a: {
//       demand: true,
//       alias: 'address',
//       describe: 'Address to fetch weather for',
//       string: true
//     }
//   })
//   .help()
//   .argv;
//
// geocode.geocodeAddress(argv.address, (errorMessage, results) => {
//   if (errorMessage) {
//     console.log(errorMessage);
//   } else {
//     console.log(JSON.stringify(results, undefined, 2));
//   }
// });
//

const request = require('request');
const app_configs = require('./configs');
const API_KEY = app_configs.API_KEY;
const LAT = 45.677;
const LNG = -115.445;


request({
  url: `https://api.darksky.net/forecast/${API_KEY}/${LAT},${LNG}`,
  json: true
},(error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log(body.currently.temperature);
  } else {
    console.log('Unable to fetch weather data.');
  }
});
