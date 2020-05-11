#!/usr/bin/node
/*
  Square #1
*/
class Square extends require('./5-square') {
  charPrint (c) {
    c = typeof c === 'undefined' ? 'X' : c;
    for (let cnt = 0; cnt < this.height; cnt++) {
      console.log(c.repeat(parseInt(this.width)));
    }
  }
}
module.exports = Square;
