#!/usr/bin/node
let num = 0;
exports.logMe = function (item) {
  const printed = [];
  printed.push(item);
  console.log(num + ': ' + item);
  num++;
};
