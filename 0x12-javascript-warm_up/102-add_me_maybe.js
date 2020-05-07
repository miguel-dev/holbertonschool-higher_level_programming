#!/usr/bin/bash
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
