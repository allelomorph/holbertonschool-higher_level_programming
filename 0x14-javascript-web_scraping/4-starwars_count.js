#!/usr/bin/node
// uses Star Wars API to display amount of films featuring Wedge Antilles
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body);
  const wedgeURL = 'https://swapi-api.hbtn.io/api/people/18/';
  let count = 0;
  for (let i = 0; i < films.results.length; i++) {
    if (films.results[i].characters.includes(wedgeURL)) {
      count += 1;
    }
  }
  console.log(count);
});
