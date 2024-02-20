#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_error, response) {
  console.log('code:', response.statusCode);
});
