#!/usr/bin/node

let printText = parseInt(process.argv[2]);
if (isNaN(printText) || process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else {
  while (printText > 0) {
    console.log('C is fun');
    printText--;
  }
}
