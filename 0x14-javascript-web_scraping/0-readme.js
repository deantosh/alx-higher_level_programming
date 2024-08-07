#!/usr/bin/node
/*
Script reads and prints the content of a file.
If an error occurs it prints the error object
*/

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
