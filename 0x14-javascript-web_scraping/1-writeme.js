#!/usr/bin/node

let filename = process.argv[2];
let text= process.argv[3];
const fs = require('fs');
fs.readFile(filename, text, 'utf-8', function(err, data){
if(err){
    console.log(err);
}
});