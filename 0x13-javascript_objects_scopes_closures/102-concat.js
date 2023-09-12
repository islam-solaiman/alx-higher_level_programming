#!/usr/bin/node

const first = require('fs');
let content = '';

content = content.concat(first.readFileSync(process.argv[2]));
content = content.concat(first.readFileSync(process.argv[3]));
first.writeFileSync(process.argv[4], content);
