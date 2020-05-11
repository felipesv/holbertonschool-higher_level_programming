#!/usr/bin/node
/*
  Log me
*/
var counter = 0;
exports.logMe = function (item) {
  console.log(counter + ':  ' + item);
  counter++;
};
