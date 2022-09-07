#!/usr/bin/node

function factorial (k) {
    if (isNaN(k) || k === 0) {
      return 1;
    } else {
      return k * factorial(k - 1);
    }
  }
  
console.log(factorial(parseInt(process.argv[2])));

