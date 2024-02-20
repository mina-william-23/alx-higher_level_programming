#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const path = process.argv[3];

request(link, (error, response, body) => {
  if (!error) {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
