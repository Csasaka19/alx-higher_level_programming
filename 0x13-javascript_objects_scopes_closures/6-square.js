#!/usr/bin/node

const SquareParent = require("./5-square");

module.exports = class Square extends SquareParent{
    constructor(size){
        super(size, size);
    }
    charPrint(c){
        this.print(c);
    }
