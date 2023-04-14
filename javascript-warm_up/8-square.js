#!/usr/bin/node
const { argv } = require('process');
const myVar = parseInt(argv[2]);
let i = 0;
let j = 0;
let line = '';

if (myVar) {
  while (i < myVar) {
    line += 'X';
    i++;
  }
  while (j < myVar) {
    console.log(line);
    j++;
  }
} else {
  console.log('Missing size');
}
