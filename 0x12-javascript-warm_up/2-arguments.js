#!/usr/bin/node
const Noargv = process.argv.length - 2;

if(Noargv === 0){
    console.log('No argument');   
}
else if(Noargv === 1){
    console.log('Argument found');   
}
else{
   console.log('Arguments found');   
}

