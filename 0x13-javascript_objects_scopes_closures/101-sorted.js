#!/usr/bin/node
// import dict from data file; creates+prints new dict {frequency: list of ids}
const dict = require('./101-data').dict;

const sortByFrequency = {};
for (const key in dict) {
  if (dict[key] in sortByFrequency) {
    sortByFrequency[dict[key]].push(key);
  } else {
    sortByFrequency[dict[key]] = [key];
  }
}
console.log(sortByFrequency);
