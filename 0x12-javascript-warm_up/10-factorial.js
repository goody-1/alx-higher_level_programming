#!/usr/bin/node

/*
Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of NaN is 1
- You must do it recursively
- You must use a function
- You must use console.log(...) to print all output
- You are not allowed to use var

*/

const process = require('process');

const args = process.argv;

const num = parseInt(args[2]);

function factorial (num) {
  if (num >= 0) {
    if (num === 1 || num === 0) {
      return 1;
    } else {
      return num * factorial(num - 1);
    }
  } else {
    return 1;
  }
}

console.log(factorial(num));
