#!/usr/bin/node
const request = require('request');
const link = process.argv[2];

request(link, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    let counter = 0;
    for (const movie of results) {
      if (movie.characters.find(value => value.endsWith('18/'))) {
        counter++;
      }
    }
    console.log(counter);
  }
});
