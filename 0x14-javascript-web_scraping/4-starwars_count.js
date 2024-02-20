#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_error, _response, body) {
  const results = JSON.parse(body).results;
  console.log(results.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0));
});
