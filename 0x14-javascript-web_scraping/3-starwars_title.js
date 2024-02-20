#!/usr/bin/node

const request = require('request');
const episode = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(episode, function (_error, _response, body) {
  console.log(JSON.parse(body).title);
});
