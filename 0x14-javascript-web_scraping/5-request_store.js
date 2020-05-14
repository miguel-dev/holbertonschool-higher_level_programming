#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);

let wpContents;
request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    wpContents = body;
    fs.writeFile(args[1], wpContents, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});
