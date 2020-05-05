#!/usr/bin/node
/*
  Call me Moby
*/
function callMeMoby (x, theFunction) {
  for (let cnt = 0; cnt < x; cnt++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
