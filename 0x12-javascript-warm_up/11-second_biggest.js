#!/usr/bin/node
// returns "second biggest" number in args (largest after removing first max)
const argvN = [];
for (let i = 0; i < process.argv.length - 2; i++) {
  argvN[i] = Math.floor(Number(process.argv[i + 2]));
}

const filtered = argvN.filter(n => !isNaN(n));
// default sort is alphabetic, see https://stackoverflow.com/questions/1063007/how-to-sort-an-array-of-integers-correctly
const sorted = filtered.sort(function (a, b) {
  return a - b;
});

if (sorted.length < 2) {
  console.log(0);
} else {
  console.log(sorted[sorted.length - 2]);
}
