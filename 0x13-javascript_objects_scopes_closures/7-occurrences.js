#!/usr/bin/node
/*
  Occurrences
*/
exports.nbOccurences = function (list, searchElement) {
  let match = 0;
  for (let cnt = 0; cnt < list.length; cnt++) {
    if (list[cnt] === searchElement) {
      match++;
    }
  }
  return match;
};
