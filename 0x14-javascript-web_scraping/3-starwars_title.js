#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(API_URL, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
