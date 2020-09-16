#!/usr/bin/node
// converts first arg to integer and prints result, or 'Not a number' if failed
const number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(number));
}
