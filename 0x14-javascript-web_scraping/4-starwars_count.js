#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    if (!body) {
      return 0;
    }
    const films = JSON.parse(body).results;
    let num = 0;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (character === 'https://swapi-api.hbtn.io/api/people/18/') {
          num++;
          break;
        }
      }
    }
    console.log(num);
  }
});
