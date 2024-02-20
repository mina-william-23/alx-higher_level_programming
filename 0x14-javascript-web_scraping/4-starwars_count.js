#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const link = `https://swapi-api.hbtn.io/api/films/${id}`;

request(link, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
