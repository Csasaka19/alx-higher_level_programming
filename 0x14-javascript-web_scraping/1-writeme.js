#!/usr/bin/node

const filename = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.readFile(filename, text, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
