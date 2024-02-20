#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(link, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const characterLink of characters) {
      request(characterLink, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
