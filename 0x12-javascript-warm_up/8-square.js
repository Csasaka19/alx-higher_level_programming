#!/usr/bin/node

const first = parseInt(process.argv[2]);

if (isNaN(first)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < first; i++) {
    console.log('X'.repeat(first));
  }
}
