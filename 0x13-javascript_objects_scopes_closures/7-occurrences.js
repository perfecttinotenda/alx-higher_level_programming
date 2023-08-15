#!/usr/bin/node

/* Learning JavaScript, Happy Coding */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0);
};
