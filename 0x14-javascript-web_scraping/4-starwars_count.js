#!/usr/bin/node
// uses Star Wars API to display amount of films featuring Wedge Antilles
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  const wedgeId = 18;
  let count = 0;
  for (const film of films) {
    for (const url of film.characters) {
      if (url.includes(
        `/api/people/${wedgeId}/`)) {
        count += 1;
      }
    }
  }
  console.log(count);
});
