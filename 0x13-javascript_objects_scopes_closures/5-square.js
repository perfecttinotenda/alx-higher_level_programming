#!/usr/bin/node

/* Learning JavaScript, Happy Coding */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
