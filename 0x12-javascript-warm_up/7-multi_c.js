#!/usr/bin/node
// prints 'C is fun' n times; n taken from first arg to script
const n = Math.floor(Number(process.argv[2]));
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
