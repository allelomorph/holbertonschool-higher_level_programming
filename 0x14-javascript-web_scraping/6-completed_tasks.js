#!/usr/bin/node
// computes the number of tasks completed by user id
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const taskList = JSON.parse(body);
  const userTotals = {};
  for (const task of taskList) {
    if (task.userId.toString() in userTotals) {
      if (task.completed === true) {
        userTotals[task.userId.toString()] += 1;
      }
    } else {
      userTotals[task.userId.toString()] = 0;
    }
  }
  const userTotalsEdit = { ...userTotals };
  for (const key in userTotalsEdit) {
    if (userTotalsEdit[key] === 0) {
      delete userTotalsEdit[key];
    }
  }
  console.log(userTotalsEdit);
});
