#!/usr/bin/node
const numberArgs = process.argv.length - 2;
if (numberArgs === 0) {
  console.log('No argument');
} else if (numberArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
