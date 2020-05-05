#!/usr/bin/node
/*
   Second biggest!
*/
if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3 && parseInt(process.argv[2]) === 1) {
  console.log(0);
} else {
  const list = [];
  let max = 0;
  for (let cnt = 2; cnt < process.argv.length; cnt++) {
    list.push(parseInt(process.argv[cnt]));
  }
  max = Math.max.apply(null, list);
  list.splice(list.indexOf(max), 1);
  max = Math.max.apply(null, list);
  console.log(max);
}
