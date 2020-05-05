#!/usr/bin/node
/*
  Value of my argument
*/
if (typeof process.argv[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
