#!/usr/bin/node
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
