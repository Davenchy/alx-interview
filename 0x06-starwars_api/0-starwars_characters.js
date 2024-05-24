#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  process.exit(1);
}

const API = 'https://swapi-api.hbtn.io/api/films/';
const movieId = parseInt(process.argv[2]);

function requestMovieCharacters (movieId) {
  return new Promise((resolve, reject) => {
    request(`${API}${movieId}`, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });
}

function downloadCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

const downloadCharacters = (characters) =>
  Promise.all(characters.map(downloadCharacter));

requestMovieCharacters(movieId)
  .then(downloadCharacters)
  .then((characters) => {
    characters.forEach((c) => console.log(c.name));
  })
  .catch(console.error);
