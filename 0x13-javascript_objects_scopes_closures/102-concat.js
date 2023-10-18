#!/usr/bin/node
const fs = require('fs');

const sourceFilePath1Arg = fs.readFileSync(process.argv[2]).toString();
const sourceFilePath2Arg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], sourceFilePath1Arg + sourceFilePath2Arg);
