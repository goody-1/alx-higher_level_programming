#!/usr/bin/node

/*
Write a script that concats 2 files.

- The first argument is the file path of the first source file
- The second argument is the file path of the second source file
- The third argument is the file path of the destination

*/

const args = require('process').argv;
const fs = require('fs');

const fileA = args[2]; const fileB = args[3]; const fileC = args[4];

const contentA = fs.readFileSync(fileA, 'utf-8') + '\n';
const contentB = fs.readFileSync(fileB, 'utf-8') + '\n';

fs.writeFileSync(fileC, contentA + contentB);
