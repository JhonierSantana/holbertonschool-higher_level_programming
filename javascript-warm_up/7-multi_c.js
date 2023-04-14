#!/usr/bin/node
const { argv } = require('process');
const myVar = parseInt(argv[2]);
let i = 0;

if (myVar) {
  while (i < myVar) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
