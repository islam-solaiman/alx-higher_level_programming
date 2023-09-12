#!/usr/bin/node

const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const val = Object.values(dict);
const valUniq = [...new Set(vals)];
const newDict = {};
for (const i in valUniq) {
  const list = [];
  for (const j in totalList) {
    if (totalList[j][1] === valsUniq[i]) {
      list.unshift(totalList[j][0]);
    }
  }
  newDict[valUniq[i]] = list;
}
console.log(newDict);
