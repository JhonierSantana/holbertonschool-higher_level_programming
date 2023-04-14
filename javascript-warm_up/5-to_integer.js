#!/usr/bin/node
const { argv } = require('process');

const myVar = parseInt(argv[2]);

if (myVar) {
  console.log(`My number: ${myVar}`);
} else {
  console.log('Not a number');
}
