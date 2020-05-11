#!/usr/bin/node
/*
  Rectangle #3
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let cntx = 0; cntx < this.height; cntx++) {
      console.log('X'.repeat(parseInt(this.width)));
    }
  }
}
module.exports = Rectangle;
