#!/usr/bin/node
// edit existing code (insert at line 8-10) to add `incr` function
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value = this.value + 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
