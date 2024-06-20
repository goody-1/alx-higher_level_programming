#!/usr/bin/node

/*
Write a script that imports an array and computes a new array.

- Your script must import list from the file 100-data.js
- You must use a map. Tips
- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list

*/

const array = require('./100-data.js').list;

const newArray = array.map((x, index) => x * index);

console.log(array); console.log(newArray);
