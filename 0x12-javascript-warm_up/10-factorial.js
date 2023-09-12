#!/usr/bin/node
function fact (n1) {
  if (isNaN(n1) || Number(n1) <= 1) {
    return 1;
  }
  return n1 * fact(n1 - 1);
}

console.log(fact(process.argv[2]));
