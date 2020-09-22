#!/usr/bin/node
// create class `Square` which inherits from `Rectangle`; adds charPrint method
const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
