#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2).map((x) => Number(x))
    .sort(function (a, b) { return b - a; });
  console.log(list[1]);
}
