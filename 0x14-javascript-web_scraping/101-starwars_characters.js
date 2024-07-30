#!/usr/bin/node

const request = require('request');

async function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterName = JSON.parse(body).name;
        resolve(characterName);
      }
    });
  });
}

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    try {
      for (const character of characters) {
        const characterName = await getCharacterName(character);
        console.log(characterName);
      }
    } catch (error) {
      console.error('Error fetching character data:', error);
    }
  }
});
