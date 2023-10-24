#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = url.concat(movieId);

request(fullUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    // Create variable to store the number of characters processed
    let charactersProcessed = 0;
    // Create empty array to store the character names
    const characterNames = [];
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const charName = JSON.parse(body).name;
          // Add character name to the array
          characterNames.push(charName);
        }
        // Increment charactersProcessed variable
        charactersProcessed++;
        // Check all characters have been processed
        if (charactersProcessed === characters.length) {
          // Log character names when all characters have been processed
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(error);
  }
});
