#!/usr/bin/node

/* Learning JavaScript, Happy Coding */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
