#!/usr/bin/node

/*
Write a function that returns the number of occurrences in a list:

- Prototype: exports.nbOccurences = function (list, searchElement)

*/

module.exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (const item of list) {
    if (item === searchElement) {
      counter++;
    }
  }
  return counter;
};
