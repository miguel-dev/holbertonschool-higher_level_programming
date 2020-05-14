#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const ctasks = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0 };

    for (const task of tasks) {
      for (let i = 0; i < 10; i++) {
        if (task.userId === i + 1 && task.completed) {
          const id = i + 1;
          ctasks[id.toString()]++;
        }
      }
    }
    console.log(ctasks);
  }
});
