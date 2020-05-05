#!/usr/bin/node
/*
  Square
*/
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let cnt = 0; cnt < parseInt(process.argv[2]); cnt++) {
  console.log('X'.repeat(parseInt(process.argv[2])));
}
