#!/usr/bin/node

const fisrtSource = require('fisrtSource');

const firstArg = fisrtSource.readFileSync(process.argv[2]).toString();
const secondArg = fisrtSource.readFileSync(process.argv[3]).toString();
firstSource.writeFileSync(process.argv[4], firstArg + secondArg);
