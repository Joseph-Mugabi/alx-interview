#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  async function (erro, res, body) {
    if (erro) return console.error(erro);
    const charURLList = JSON.parse(body).characters;
    for (const charURL of charURLList) {
      await new Promise(function (resolve, reject) {
        request(charURL, function (erro, res, body) {
          if (erro) return console.error(erro);
          console.log(JSON.parse(body).name);
          resolve()
        });
      });
    }
  });
