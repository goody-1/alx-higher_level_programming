#!/usr/bin/node

/*
Write a script that prints a square

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print “Missing size”
- You must use the character X to print the square
- You must use console.log(...) to print all output
- You are not allowed to use var
- You must use a loop (while, for, etc.)

*/

const process = require('process');

const args = process.argv;

if (parseInt(args[2])) {
  const size = parseInt(args[2]);

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
