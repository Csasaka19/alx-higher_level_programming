#!/usr/bin/node

const convert = parseInt(process.argv[2]);

if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convert);
}
