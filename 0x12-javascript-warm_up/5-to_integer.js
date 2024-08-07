#!/usr/bin/node
/*Script prints My number: <first argument converted in integer>.
If the first argument can be converted to an integer.
*/
if (process.argv[2]) {
  const num = parseInt(process.argv[2]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + Math.floor(num));
  }
} else {
  console.log('Not a number');
}
