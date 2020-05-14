#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let num = 0;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (character.endsWith('/18/')) {
          num++;
        }
      }
    }
    console.log(num);
  }
});
