#!/usr/bin/node
// imports array from data file; creates new array with map; prints both
const list = require('./100-data').list;

const newList = list.map(n => n * list.indexOf(n));
console.log(list);
console.log(newList);
