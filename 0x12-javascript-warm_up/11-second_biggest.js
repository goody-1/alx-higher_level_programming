#!/usr/bin/node

/*
Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print 0
- If the number of arguments is 1, print 0
- You must use console.log(...) to print all output
- You are not allowed to use var

*/

const process = require('process');

const args = process.argv.slice(2);
const list = [];

if (args.length > 1) {
  for (let i = 0; i < args.length; i++) {
    list.push(parseInt(args[i]));
  }
  const largest = Math.max(...list);

  list.splice(list.indexOf(largest), 1);

  console.log(Math.max(...list));
} else {
  console.log(0);
}
