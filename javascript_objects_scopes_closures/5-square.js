#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (w, h, size) {
    super(w, h);
  }
}
module.exports = Square;
