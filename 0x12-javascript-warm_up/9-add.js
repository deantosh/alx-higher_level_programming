#!/usr/bin/node
// Script prints the addition of 2 integers.
if (process.argv.length === 4) {
  const num1 = parseInt(process.argv[2]);
  const num2 = parseInt(process.argv[3]);
  if (isNaN(num1) || isNaN(num2)) {
    console.log('NaN');
  } else {
    console.log(num1 + num2);
  }
} else {
  console.log('NaN');
}
