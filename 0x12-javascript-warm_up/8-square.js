#!/usr/bin/node

let size = parseInt(process.argv[2]);
if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let chr = 'X';
for (let i = 1; i < size; i++) {
  chr += 'X';
}
while (size > 0) {
  console.log(chr);
  size--;
}
