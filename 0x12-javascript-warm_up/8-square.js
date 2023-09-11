#!/usr/bin/node
let agv = process.argv[2];
agv = Number(agv);
if (isNaN(agv)) {
  console.log('Missing size');
} else {
  let row;
  for (let i = 0; i < agv; i++) {
    row = '';
    for (let j = 0; j < agv; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
