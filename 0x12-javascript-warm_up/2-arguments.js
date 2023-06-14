#!/usr/bin/node
const argmt = process.argv.lenght;
if(argmt === 2) {
  console.log('No argument');
} else if (argmt === 3) {
  console.log('Argument found');
} else if (argmt > 3) {
  console.log('Agument found');
}
