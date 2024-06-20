#!/usr/bin/node

/*
Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

- You must use the class notation for defining your class and extends
- The constructor must take 1 argument: size
- The constructor of Rectangle must be called (by using super())

*/

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
