#!/usr/bin/node
// imports array from data file; creates new array with map; prints both
list = require('./100-data').list;
const listDoubled = list.map(n => n * 2);
console.log(list);
console.log(listDoubled);
