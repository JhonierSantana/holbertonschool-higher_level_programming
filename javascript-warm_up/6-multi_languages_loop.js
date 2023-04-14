#!/usr/bin/node
const { argv } = require('process');

const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (argv[2] of myArray) {
  console.log(argv[2]);
}
