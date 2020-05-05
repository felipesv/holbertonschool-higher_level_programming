#!/usr/bin/node
/*
  Factorial
*/
function factorial (num) {
  if (isNaN(parseInt(num))) {
    return 1;
  } else if (parseInt(num) === 0) {
    return 1;
  } else {
    return parseInt(num) * factorial(parseInt(num) - 1);
  }
}

console.log(factorial(process.argv[2]));
