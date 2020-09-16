#!/usr/bin/node
// prints first arg passed to script, or 'No argument' if no args
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
