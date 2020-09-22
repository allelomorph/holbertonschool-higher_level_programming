#!/usr/bin/node
// uses Star Wars API to display title of film by id/release order
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const film = JSON.parse(body);
  console.log(film.title);
});
