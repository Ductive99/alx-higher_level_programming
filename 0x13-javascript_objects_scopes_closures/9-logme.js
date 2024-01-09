#!/usr/bin/node
// Prints the nbr of args already printed and the new argument value.

let nbr = 0;

exports.logMe = function count (item) {
  console.log(`${nbr}: ${item}`);
  nbr += 1;
};
