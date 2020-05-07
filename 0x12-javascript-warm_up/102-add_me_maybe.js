#!/usr/bin/bash
exports.addMeMaybe = function (number, theFunction) {
  n = ++number;
  theFunction();
};
