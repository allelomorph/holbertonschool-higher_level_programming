#!/usr/bin/node
// defines function that returns the total occurances of an element in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
};
