#!/usr/bin/node
/*
  Esrever
*/
exports.esrever = function (list) {
  const list2 = [];
  for (let cnt = list.length - 1; cnt >= 0; cnt--) {
    list2.push(list[cnt]);
  }
  return list2;
};
