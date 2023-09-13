#!/usr/bin/node
const myList = require('./100-data').list;
console.log(myList);
console.log(myList.map((item, idx) => item * idx));
