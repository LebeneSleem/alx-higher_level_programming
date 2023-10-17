#!/usr/bin/node

const MainSquare = require('./5-square');

class Square extends MainSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;
