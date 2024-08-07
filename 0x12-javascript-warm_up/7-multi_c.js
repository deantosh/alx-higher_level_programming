#!/usr/bin/node
// Script prints x times "C is fun".
if (process.argv[2]) {
  const num = process.argv[2];
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
