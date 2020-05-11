#!/usr/bin/node
/*
  Sorted occurences
*/
const dict1 = require('./101-data.js').dict;
const dict2 = {};
for (const key in dict1) {
  const list = dict2[dict1[key]] ? dict2[dict1[key]] : [];
  list.push(key);
  dict2[dict1[key]] = list;
}
console.log(dict2);
