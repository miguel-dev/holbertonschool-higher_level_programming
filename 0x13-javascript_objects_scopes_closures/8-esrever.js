#!/usr/bin/node
exports.esrever = function (list) {
  let start = 0;
  let end = list.length - 1;
  while (start < end) {
    const swap = list[start];
    list[start] = list[end];
    list[end] = swap;
    start++;
    end--;
  }
  return list;
};
