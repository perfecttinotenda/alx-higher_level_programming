#!/usr/bin/node

/* Learning JavaScript, Happy Coding */
exports.logMe = function (item) {
  if (typeof this.count === 'undefined') {
    this.count = 0;
  }
  console.log(this.count + ': ' + item);
  this.count++;
};
