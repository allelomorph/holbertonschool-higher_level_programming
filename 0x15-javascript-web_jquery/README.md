# (305) 0x15. Javascript - Web JQuery
Foundations > Higher-level programming > JavaScript

---

### Project author
Guillaume Salva

### Assignment dates
09-24-2020 to 09-25-2020

### Description
Using JavaScript and JQuery to get and modify HTML, JQuery Ajax to handle HTTP requests, and JavaScript to listen and bind to user or DOM events.

### Provided file(s)
* [`0-main.html`](./tests/0-main.html) [`1-main.html`](./tests/1-main.html) [`2-main.html`](./tests/2-main.html) [`3-main.html`](./tests/3-main.html) [`4-main.html`](./tests/4-main.html) [`5-main.html`](./tests/5-main.html) [`6-main.html`](./tests/6-main.html) [`7-main.html`](./tests/7-main.html) [`8-main.html`](./tests/8-main.html) [`9-main.html`](./tests/9-main.html)
* [`100-main.html`](./tests/100-main.html) [`101-main.html`](./tests/101-main.html) [`102-main.html`](./tests/102-main.html) [`103-main.html`](./tests/103-main.html)

---

## Mandatory Tasks

### :white_check_mark: 0. No JQuery
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
* You must use `document.querySelector` to select the HTML tag
* You can’t use the JQuery API
* Test with [`0-main.html`](./tests/0-main.html) in your browser

File(s): [`0-script.js`](./0-script.js)

### :white_check_mark: 1. With JQuery
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`1-main.html`](./tests/1-main.html) in your browser

File(s): [`1-script.js`](./1-script.js)

### :white_check_mark: 2. Click and turn red
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`2-main.html`](./tests/2-main.html) in your browser

File(s): [`2-script.js`](./2-script.js)

### :white_check_mark: 3. Add `.red` class
Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`3-main.html`](./tests/3-main.html) in your browser

File(s): [`3-script.js`](./3-script.js)

### :white_check_mark: 4. Toggle classes
Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:
* The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
* If the current class is `red`, when the user clicks on `DIV#toggle_header`, the class must be updated to `green`; and the reverse.
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`4-main.html`](./tests/4-main.html) in your browser

File(s): [`4-script.js`](./4-script.js)

### :white_check_mark: 5. List of elements
Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:
* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`5-main.html`](./tests/5-main.html) in your browser

File(s): [`5-script.js`](./5-script.js)

### :white_check_mark: 6. Change the text
Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`
* You can’t use document.querySelector to select the HTML tag
* You must use the JQuery API
* Test with [`6-main.html`](./tests/6-main.html) in your browser

File(s): [`6-script.js`](./6-script.js)

### :white_check_mark: 7. Star wars character
Write a JavaScript script that fetches the character name from this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`
* The name must be displayed in the HTML tag `DIV#character`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`7-main.html`](./tests/7-main.html) in your browser

File(s): [`-script.js`](./-script.js)

### :white_check_mark: 8. Star Wars movies
Write a JavaScript script that fetches and lists the title for all movies by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`
* All movie titles must be list in the HTML tag `UL#list_movies`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Test with [`8-main.html`](./tests/8-main.html) in your browser

File(s): [`8-script.js`](./8-script.js)

### :white_large_square: 9. Say Hello!
Write a JavaScript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of hello from that fetch in the HTML tag `DIV#hello`.
* The translation of “hello” must be displayed in the HTML tag DIV#hello
* You can’t use document.querySelector to select the HTML tag
* You must use the JQuery API
* Your script must work when it is imported from the <head> tag
* Test with [`9-main.html`](./tests/9-main.html) in your browser

## Advanced Tasks

### :white_check_mark: 10. No jQuery - document loaded
Write a JavaScript script that updates the text color of the <header> element to red (`#FF0000`):
* You must use `document.querySelector` to select the HTML tag
* You can’t use the jQuery API
* Note: Your script must be imported from the `<head>` tag, not at the end of the HTML
* Test with [`100-main.html`](./tests/100-main.html) in your browser

File(s): [`100-script.js`](./100-script.js)

### :white_check_mark: 11. List, add, remove
Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:
* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* When the user clicks on `DIV#add_item`: a new element is added to the list
* When the user clicks on `DIV#remove_item`: the last element is removed from the list
* When the user clicks on `DIV#clear_list`: all elements of the list are removed
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* You script must work when it imported from the `HEAD` tag
* Test with [`101-main.html`](./tests/101-main.html) in your browser

File(s): [`101-script.js`](./101-script.js)

### :white_check_mark: 12. Say hello to everybody!
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
* The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
* The translation must be fetched when the user clicks on `INPUT#btn_translate`
* The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the `<head>` tag
* Test with [`102-main.html`](./tests/102-main.html) in your browser

File(s): [`102-script.js`](./102-script.js)

### :white_check_mark: 13. And press ENTER
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
* The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
* The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
* The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the <head> tag
* Test with [`103-main.html`](./tests/103-main.html) in your browser

File(s): [`103-script.js`](./103-script.js)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
