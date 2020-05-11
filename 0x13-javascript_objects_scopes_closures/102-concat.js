#!/usr/bin/node
/*
  Concat files
*/
const fs = require('fs');
let text = '';
text += fs.readFileSync(process.argv[2], 'utf8');
text += fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], text);
