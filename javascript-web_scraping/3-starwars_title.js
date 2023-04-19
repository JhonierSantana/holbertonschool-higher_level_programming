#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const conver = JSON.parse(body);
    console.log(`${conver.title}`);
  }
});
