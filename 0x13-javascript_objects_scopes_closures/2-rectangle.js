#!/usr/bin/node
/*
Script defines a `Rectangle` class, that initializes object if w > 0 and h > 0.
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
