#!/usr/bin/node

let first = parseInt(process.argv[2]);
let second = parseInt(process.argv[3]);

function add(a, b){
if(isNaN(a) || isNaN(b)){
    return NaN;
}
else{
    return a + b;
}
}

console.log(add(first, second));

