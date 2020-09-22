#!/usr/bin/node
// defines function that converts a number from base 10 to `base`
exports.converter = function (base) {
  return function (value) {
    return value.toString(base);
  };
};
