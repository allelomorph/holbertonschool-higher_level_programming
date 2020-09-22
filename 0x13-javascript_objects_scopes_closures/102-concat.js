#!/usr/bin/node
// reads two text files and concatenates contents into new file
const fs = require('fs');
// fs is standard but needs import

// each `readFile` and `writeFile` call is asynchronous
fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;
  // data is bytestream before encoding
  let output = data;
  fs.readFile(process.argv[3], (err, data) => {
    if (err) throw err;
    output += data;
    fs.writeFile(process.argv[4], output, (err) => {
      if (err) throw err;
    });
  });
});
