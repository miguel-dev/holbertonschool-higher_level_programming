#!/usr/bin/node
const listArgs = process.argv.slice(2, process.argv.length);

if (listArgs.length < 2) {
  console.log(0);
} else {
  for (let i = 0; i < listArgs.length; i++) {
    listArgs[i] = parseInt(listArgs[i]);
  }
  listArgs.sort(function (a, b) { return b - a; });
  console.log(listArgs[1]);
}
