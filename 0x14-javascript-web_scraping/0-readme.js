#!/usr/bin/node
/*
  Readme
*/
const fs = require('fs');
try {
  console.log(fs.readFileSync(process.argv[2], 'utf-8'));
} catch (error) {
  console.log(error);
}
