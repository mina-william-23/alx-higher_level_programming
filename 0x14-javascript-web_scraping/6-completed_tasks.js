#!/usr/bin/node
const request = require('request');
const link = process.argv[2];

request(link, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const result = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (todo.userId in result) {
          result[todo.userId]++;
        } else {
          result[todo.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
