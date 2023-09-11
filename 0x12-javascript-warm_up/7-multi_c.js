#!/usr/bin/node
let agv = process.argv[2];
if (typeof agv !== 'undefined') {
  if (isNaN(agv)) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < agv; i++) {
      console.log('C is fun');
    }
  }
}
