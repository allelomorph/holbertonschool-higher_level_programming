#!/usr/bin/node
// using Star Wars API, prints all characters of a given film
const request = require('request');

const filmsURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(filmsURL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const urlList = JSON.parse(body).characters;
  for (const url of urlList) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
