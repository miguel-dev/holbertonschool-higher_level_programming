#!/usr/bin/node
const fs = require('fs');

const fpath = process.argv[2];
fs.readFile(fpath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
