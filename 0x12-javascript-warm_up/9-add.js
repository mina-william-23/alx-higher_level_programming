#!/usr/bin/node
const n1 = process.argv[2];
const n2 = process.argv[3];
if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  console.log(`${Number(n1) + Number(n2)}`);
}
