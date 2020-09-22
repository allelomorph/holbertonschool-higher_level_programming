#!/usr/bin/node
// writes string to a file
const fs = require('fs');

let filename = '';
if (process.argv[2] !== undefined) {
  filename = process.argv[2];
}
fs.writeFile(filename, process.argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
