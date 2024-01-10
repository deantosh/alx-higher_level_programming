#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let rect = '';
        for (let j = 0; j < this.width; j++) {
          rect += 'C';
        }
        console.log(rect);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
