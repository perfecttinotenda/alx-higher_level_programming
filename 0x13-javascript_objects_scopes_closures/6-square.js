#!/usr/bin/node

/* Learning JavaScript, Happy Coding */
const supSquare = require('./5-square');

class Square extends supSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
