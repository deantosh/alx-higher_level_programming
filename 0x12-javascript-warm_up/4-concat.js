#!/usr/bin/node
const arg = 'undefined';
if (process.argv.length === 2) {
  console.log(arg + ' is ' + arg);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
