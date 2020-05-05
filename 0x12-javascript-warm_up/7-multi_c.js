#!/usr/bin/node
/*
  I love C
*/
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
for (let cnt = 0; cnt < parseInt(process.argv[2]); cnt++) {
  console.log('C is fun');
}
