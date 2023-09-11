#!/usr/bin/node
const agv = process.argv.length;
if (agv === 2) {
  console.log('No argument');
} else if (agv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
