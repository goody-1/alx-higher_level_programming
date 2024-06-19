#!/usr/bin/node

/**
 * callMeMoby - function that executes a function x times.
 * @x: number of times to execute the function.
 * @theFunction: function to be executed.
 */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
