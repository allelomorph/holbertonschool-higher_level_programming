#!/usr/bin/node
// prints factorial of first arg given to script, uses recursive function
function factorial (number) {
  if (number > 1) {
    return number * factorial(number - 1);
  } else {
    return 1;
  }
}
const n = Math.floor(Number(process.argv[2]));
console.log(factorial(n));
