#!/usr/bin/node

const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else if (c === 'C') {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
};
