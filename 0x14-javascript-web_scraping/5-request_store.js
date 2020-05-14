#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);

request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(args[1], body, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
