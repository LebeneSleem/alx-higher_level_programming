#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const wedgeAntillesMovies = films.filter((film) => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(wedgeAntillesMovies.length);
  } else {
    console.error(`Failed to retrieve information. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
