#!/usr/bin/node
const request = require('request');
const util = require('util');

const promiseR = util.promisify(request);
const [, , id] = process.argv;

const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function fetchData (url) {
  try {
    const body = (await promiseR(url)).body;
    const data = JSON.parse(body);

    for (const character of data.characters) {
      try {
        const charData = (await promiseR(character)).body;
        const charName = JSON.parse(charData).name;
        console.log(charName);
      } catch (err) {
        console.log(err);
      }
    }
  } catch (err) {
    console.log(err);
  }
}

fetchData(URL);
