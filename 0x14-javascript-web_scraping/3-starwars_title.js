#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;
request(endpoint, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
