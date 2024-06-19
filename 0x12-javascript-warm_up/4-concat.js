#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”

const process = require('process');

const args = process.argv;

if (args.length < 3) {
  console.log('undefined is undefined');
} else if (args.length === 3) {
  console.log(args[2] + ' is undefined');
} else if (args.length === 4) {
  console.log(args[2] + ' is ' + args[3]);
} else {
  console.log('You need to pass just two arguments');
}
