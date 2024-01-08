#!/usr/bin/node

let num = parseInt(process.argv[2]);
if (isNaN(num) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
