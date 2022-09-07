#!/usr/bin/node
let x = parseInt(process.argv[2]);
let i = 1;
if(isNaN(x)){
    console.log('Missing number of occurrences');
}
else{
for(i = 1; i <= x; i++){
    console.log('C is fun');
}
}

