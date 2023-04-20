#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const completedTask = {};

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const obt = JSON.parse(body);
    for (const ent of obt) {
      if (ent.completed) {
        const userId = ent.userId;
        if (Object.keys(completedTask).includes(String(userId))) {
          completedTask[userId] += 1;
        } else {
          completedTask[userId] = 1;
        }
      }
    }
  }
});
