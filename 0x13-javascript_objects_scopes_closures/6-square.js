#!/usr/bin/node
class Square extends require('./5-square') {
  charPrint (c) {
    super.print(c);
  }
}
module.exports = Square;
