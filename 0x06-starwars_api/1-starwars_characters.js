#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

if (!movieID) {
	console.log('Usage: ./script.js <Movie ID>');
	process.exit(1);
}

const movieURL = 'https://swapi-api.hbtn.io/api/films/${movieID}/';

request(movieURL, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
		process.exit(1);
	}

	if (response.statusCode !== 200) {
		console.error(`Request failed with status code: ${response.statusCode}`);
 		process.exit(1);
	}

	const movieData = JSON.parse(body);
	const characterURLs = movieData.characters;

	fetchCharacterNames(characterURLs);
});

function fetchCharacterNames(urls) {
	let fetched = 0;

	urls.forEach((url) => {
		request(url, (error, response, body) => {
			if (error) {
				console.error('Error:', error);
			} else {
				const characterData = JSON.parse(body);
				console.log(characterData.name);
			}

			fetched++;

			if (fetched === urls.length) {
				process.exit(0);
			}
		});
	});
}
