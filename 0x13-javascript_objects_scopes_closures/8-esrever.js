#!/usr/bin/node
// defines function that returns a reversed array
exports.esrever = function (list) {
  const reversed = [list.length];
  for (let i = 0; i < list.length; i++) {
    reversed[list.length - (i + 1)] = list[i];
  }
  return reversed;
};
