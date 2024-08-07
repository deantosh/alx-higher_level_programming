#!/usr/bin/node
/*
Script writes a string to a file.
Arguments:
  - The first argument is the file path.
  - The second argument is the string to write to the file
Error:
 - If an error occurs print the error object.
*/

const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(file, str, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
