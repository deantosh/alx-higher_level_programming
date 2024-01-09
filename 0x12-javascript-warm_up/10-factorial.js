#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (process.argv.length === 3) {
  const num = parseInt(process.argv[2]);
  if (isNaN(num)) {
    console.log(1);
  } else {
    const result = factorial(num);
    console.log(result);
  }
  // pass num to factorial func.
} else {
  console.log(1);
}
