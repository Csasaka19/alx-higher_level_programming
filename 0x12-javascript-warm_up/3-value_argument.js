#!/usr/bin/node
const Firstarg = process.argv[2];

if (Firstarg === undefined) {
  console.log('No argument');
} else {
  console.log(Firstarg);
}
