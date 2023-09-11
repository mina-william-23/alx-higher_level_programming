#!/usr/bin/node
let agv = process.argv[2];
if (typeof agv !== 'undefined') {
  if (isNaN(agv)) {
    console.log('Missing number of occurrences');
  } else {
    agv = Number(agv);
    while (agv--) {
      console.log('C is fun');
    }
  }
}
