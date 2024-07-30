#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmData = JSON.parse(body).results;
    const movieCount = filmData.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith(`${characterId}/`))
        ? count + 1
        : count;
    }, 0);

    console.log(movieCount);
  }
});
