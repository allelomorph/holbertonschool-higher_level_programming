#!/usr/bin/node
// imports array from data file; creates new array with map; prints both
const list = require('./100-data').list;

console.log(list);
if (Array.isArray(list) && list.every(n => typeof n === 'number')) {
  const newList = list.map(n => n * list.indexOf(n));
  console.log(newList);
} else {
  console.log(undefined);
}
