#!/usr/bin/node
/*
Write a class Square that defines a square and inherits from Square of 5-square.js:
Requirements:
 - You must use the class notation for defining your class and extends
 - Create an instance method called charPrint(c) that prints the rectangle using the character c
 - If c is undefined, use the character X
*/
const SquarePrev = require('./5-square');
class Square extends SquarePrev {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let rect = '';
        for (let j = 0; j < this.width; j++) {
          rect += c;
        }
        console.log(rect);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
