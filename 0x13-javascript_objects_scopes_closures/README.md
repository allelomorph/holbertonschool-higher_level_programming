# (304) 0x13. Javascript - Objects, Scopes and Closures
Foundations > Higher-level programming > JavaScript

---

### Project author
Guillaume Salva

### Assignment dates
09-21-2020 to 09-22-2020

### Description
Introduction to Object-Oriented Programming in JavaScript: objects, classes, inheritance, scope, closure, `this`, and `undefined`.

### Provided file(s)
* [`0-main.js`](./tests/0-main.js) [`1-main.js`](./tests/1-main.js) [`2-main.js`](./tests/2-main.js) [`3-main.js`](./tests/3-main.js) [`4-main.js`](./tests/4-main.js) [`5-main.js`](./tests/5-main.js) [`6-main.js`](./tests/6-main.js) [`7-main.js`](./tests/7-main.js) [`8-main.js`](./tests/8-main.js) [`9-main.js`](./tests/9-main.js) [`10-main.js`](./tests/10-main.js)
* [`100-data.js`](./tests/100-data.js) [`101-data.js`](./tests/101-data.js)

---

## Mandatory Tasks

### :white_check_mark: 0. Rectangle #0
Write an empty class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class

File(s): [`0-rectangle.js`](./0-rectangle.js)

### :white_check_mark: 1. Rectangle #1
Write a class `Rectangle` that defines a rectangle, as with `0-rectangle.js`, which adds the following:
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`

File(s): [`1-rectangle.js`](./1-rectangle.js)

### :white_check_mark: 2. Rectangle #2
Write a class `Rectangle` that defines a rectangle, as with `1-rectangle.js`, which adds the following:
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object

File(s): [`2-rectangle.js`](./2-rectangle.js)

### :white_check_mark: 3. Rectangle #3
Write a class `Rectangle` that defines a rectangle, as with `2-rectangle.js`, which adds the following:
* Create an instance method called print() that prints the rectangle using the character `X`

File(s): [`3-rectangle.js`](./3-rectangle.js)

### :white_check_mark: 4. Rectangle #4
Write a class `Rectangle` that defines a rectangle, as with `3-rectangle.js`, which adds the following:
* Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
* Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

File(s): [`4-rectangle.js`](./4-rectangle.js)

### :white_check_mark: 5. Square #0
Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
* You must use the `class` notation for defining your class and `extends`
* The constructor must take 1 argument: `size`
* The constructor of `Rectangle` must be called (by using `super()`)

File(s): [`5-square.js`](./5-square.js)

### :white_check_mark: 6. Square #1
Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:
* You must use the `class` notation for defining your class and `extends`
* Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
    * If `c` is undefined, use the character `X`

File(s): [`6-square.js`](./6-square.js)

### :white_check_mark: 7. Occurrences
Write a function that returns the number of occurrences in a list:
* Prototype: `exports.nbOccurences = function (list, searchElement)`

File(s): [`7-occurrences.js`](./7-occurrences.js)

### :white_check_mark: 8. Esrever
Write a function that returns the reversed version of a list:
* Prototype: `exports.esrever = function (list)`
* You are not allow to use the built-in method `reverse`

File(s): [`8-esrever.js`](./8-esrever.js)

### :white_check_mark: 9. Log me
Write a function that prints the number of arguments already printed and the new argument value.
* Prototype: `exports.logMe = function (item)`
* Output format: `<number arguments already printed>: <current argument value>`

File(s): [`9-logme.js`](./9-logme.js)

### :white_check_mark: 10. Number conversion
Write a function that converts a number from base 10 to another base passed as argument:
* Prototype: `exports.converter = function (base)`
* You are not allowed to import any file
* You are not allowed to declare any new variable (`var`, `let`, etc..)

File(s): [`10-converter.js`](./10-converter.js)

## Advanced Tasks

### :white_check_mark: 11. Factor index
Write a script that imports an array and computes a new array.
* Your script must import list from the file `100-data.js`
* You must use a [`map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
* A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
* Print both the initial list and the new list

File(s): [`100-map.js`](./100-map.js)

### :white_check_mark: 12. Sorted occurences
Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
* Your script must import `dict` from the file `101-data.js`
* In the new dictionary:
    * A key is a number of occurrences
    * A value is the list of user ids
* Print the new dictionary at the end

File(s): [`101-sorted.js`](./101-sorted.js)

### :white_check_mark: 13. Concat files
Write a script that concats 2 files.
* The first argument is the file path of the first source file
* The second argument is the file path of the second source file
* The third argument is the file path of the destination

File(s): [`102-concat.js`](./102-concat.js)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
