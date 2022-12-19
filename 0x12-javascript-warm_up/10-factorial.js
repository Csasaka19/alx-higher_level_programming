#!/usr/bin/node

const factor = process.argv[2];

function factorial (k) {
  if (isNaN(k) || k === 0) {
    return 1;
  } else {
    return k * factorial(k - 1);
  }
}

console.log(factorial(parseInt(factor)));
