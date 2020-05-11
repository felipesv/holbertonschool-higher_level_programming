#!/usr/bin/node
/*
  Factor index
*/
const list1 = require('./100-data.js').list;
const list2 = list1.map((x, index) => x * index);
console.log(list1);
console.log(list2);
