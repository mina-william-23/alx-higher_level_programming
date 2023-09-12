#!/usr/bin/node
if (process.argv.length <= 4) {
  console.log(0);
} else {
  // create array from index 2
  let args = process.argv.slice(2);
  // convert it to array of numbers
  args = args.map((item) => parseInt(item));
  // sort it decreasing
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
