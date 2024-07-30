#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
