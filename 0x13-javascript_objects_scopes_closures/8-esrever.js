#!/usr/bin/node
// defines function that returns a reversed array
exports.esrever = function (list) {
  if (Array.isArray(list)) {
    const reversed = Array(list.length);
    for (let i = 0; i < list.length; i++) {
      reversed[list.length - (i + 1)] = list[i];
    }
    return reversed;
  }
};
