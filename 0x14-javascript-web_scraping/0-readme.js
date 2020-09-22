#!/usr/bin/node
// reads and prints contents of a file
const fs = require('fs');

let filename = '';
if (process.argv[2] !== undefined) {
  filename = process.argv[2];
}
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
