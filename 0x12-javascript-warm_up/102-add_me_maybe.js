#!/usr/bin/node
// defines a named function for export
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
