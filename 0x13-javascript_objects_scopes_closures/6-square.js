#!/usr/bin/node
// Creates the Square class, inherited from the previous Square class

const prevClass = require('./5-square');

module.exports = class Square extends prevClass {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
