#!/usr/bin/node
const len = process.argv.length;
if (len > 3) {
  const numArray = [];
  for (let i = 2; i < len; i++) {
    numArray.push(parseInt(process.argv[i]));
  }
  console.log(numArray);
  numArray.sort(function (a, b) { return a - b; });
  console.log(numArray[len - 4]);
} else {
  console.log(0);
}
