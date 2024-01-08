#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const nums = [];
  for (let i = 2; i < size; i++) {
    nums[i - 2] = parseInt(process.argv[i]);
  }
  nums.sort(function (a, b) { return b - a; });
  console.log(nums[1]);
}
