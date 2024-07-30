#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const tData = {};

    data.forEach(element => {
      const userId = element.userId;
      if (element.completed) {
        if (Object.prototype.hasOwnProperty.call(tData, userId)) {
          tData[userId] += 1;
        } else {
          tData[userId] = 1;
        }
      }
    });
    console.log(tData);
  }
});
