#!/usr/bin/node
/*
  Number conversion
*/
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
