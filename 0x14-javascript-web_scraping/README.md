# (333) 0x14. JavaScript - Web scraping
Foundations > Higher-level programming > JavaScript

---

### Project author
Guillaume Salva

### Assignment dates
09-22-2020 to 09-23-2020

### Description
Pulling JSON data from the web using JavaScript's `request` module and Fetch API to make HTTP requests, plus file I/O with the `fs` module.

---

## Mandatory Tasks

### :white_check_mark: 0. Readme
Write a script that reads and prints the content of a file.
* The first argument is the file path
* The content of the file must be read in `utf-8`
* If an error occurred during the reading, print the error object

File(s): [`0-readme.js`](./0-readme.js)

### :white_check_mark: 1. Write me
Write a script that writes a string to a file.
* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in `utf-8`
* If an error occurred during while writing, print the error object

File(s): [`1-writeme.js`](./1-writeme.js)

### :white_check_mark: 2. Status code
Write a script that display the status code of a `GET` request.
* The first argument is the URL to request (`GET`)
* The status code must be printed like this: `code: <status code>`
* You must use the module `request`

File(s): [`2-statuscode.js`](./2-statuscode.js)

### :white_check_mark: 3. Star Wars movie title
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
* The first argument is the movie ID
* You must use the [Star Wars API](https://swapi-api.hbtn.io/) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
* You must use the module `request`

File(s): [`3-starwars_title.js`](./3-starwars_title.js)

### :white_check_mark: 4. Star Wars Wedge Antilles
Write a script that prints the number of movies where the character “Wedge Antilles” is present.
* The first argument is the API URL of the [Star Wars API](https://swapi-api.hbtn.io/): `https://swapi-api.hbtn.io/api/films/`
* Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
* You must use the module `request`

File(s): [`4-starwars_count.js`](./4-starwars_count.js)

### :white_check_mark: 5. Loripsum
Write a script that gets the contents of a webpage and stores it in a file.
* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module `request`
* `https://loripsum.net/api` is an easy test URL

File(s): [`5-request_store.js`](./5-request_store.js)

### :white_check_mark: 6. How many completed? 
Write a script that computes the number of tasks completed by user id.
* The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
* Only print users with completed task
* You must use the module `request`

File(s): [`6-completed_tasks.js`](./6-completed_tasks.js)

## Advanced Tasks

### :white_check_mark: 7. Who was playing in this movie?
Write a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name by line
* You must use the [Star Wars API](https://swapi-api.hbtn.io/)
* You must use the module `request`

File(s): [`100-starwars_characters.js`](./100-starwars_characters.js)

### :white_check_mark: 8. Right order
Write a script that prints all characters of a Star Wars movie:
* The first argument is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name by line in the same order of the list “characters” in the `/films/` response
* You must use the [Star Wars API](https://swapi-api.hbtn.io/)
* You must use the module `request`

File(s): [`101-starwars_characters.js`](./101-starwars_characters.js)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
