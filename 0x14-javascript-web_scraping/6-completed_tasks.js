#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const ctasks = {};

    for (const task of tasks) {
      if (task.completed && !ctasks[task.userId]) {
        ctasks[task.userId] = 1;
      } else if (task.completed) {
        ctasks[task.userId]++;
      }
    }
    console.log(ctasks);
  }
});
