#!/usr/bin/node
// defines function that prints total number prior arguments plus current arg
// example of closure
exports.logMe = (function (item) {
  let itemCount = -1;
  return function (item) {
    itemCount += 1;
    console.log(itemCount + ': ' + item);
  };
})();
