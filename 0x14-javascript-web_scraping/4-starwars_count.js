#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    let num = 0;
    for (const film of films) {
      const characters = film.characters;
      if (!characters) {
        continue;
      }
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
