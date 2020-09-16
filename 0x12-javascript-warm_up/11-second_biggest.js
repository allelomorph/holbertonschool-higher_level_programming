#!/usr/bin/node
// returns "second biggest" number in args (largest after removing first max)
const argvN = [];
for (let i = 0; i < process.argv.length - 2; i++) {
  argvN[i] = Math.floor(Number(process.argv[i + 2]));
}
const filtered = argvN.filter(n => !isNaN(n));
const sorted = filtered.sort();
if (sorted.length < 2) {
  console.log(0);
} else {
  console.log(sorted[sorted.length - 2]);
}
