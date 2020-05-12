#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    this.print(c);
  }
}
module.exports = Square;
