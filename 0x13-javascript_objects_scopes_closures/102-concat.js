#!/usr/bin/node
const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).tioString();
const sArg = fs.readFileSync(process.argv[3]).tioString();
fs.writeFileSync(process.argv[4], fArg + sArg);
