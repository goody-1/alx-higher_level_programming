#!/usr/bin/node

/*
Write a function that returns the reversed version of a list:

- Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse

*/

module.exports.esrever = function (list) {
  const reversed = [];
  const len = list.length;

  for (let i = 0; i < len; i++) {
    reversed.push(list[len - 1 - i]);
  }
  return reversed;
};
