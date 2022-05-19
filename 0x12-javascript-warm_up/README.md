# (303) 0x12. Javascript - Warm up
Foundations > Higher-level programming > JavaScript

---

### Project author
Guillaume Salva

### Assignment dates
09-15-2020 to 09-16-2020

### Description
A simple introduction to JavaScript, and its use as a scripting language and for web front-end.

### Provided file(s)
* original incomplete versions of [`12-object.js`](./12-object.js) [`103-object_fct.js`](./103-object_fct.js)

---

## Mandatory Tasks

### :white_check_mark: 0. First constant, first print
Write a script that prints “JavaScript is amazing”:
* You must create a constant variable called `myVar` with the value “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File(s): [`0-javascript_is_amazing.js`](./0-javascript_is_amazing.js)

### :white_check_mark: 1. 3 languages
Write a script that prints 3 lines:
* The first line: `C is fun`
* The second line: `Python is cool`
* The third line: `JavaScript is amazing`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File(s): [`1-multi_languages.js`](./1-multi_languages.js)

### :white_check_mark: 2. Arguments
Write a script that prints a message depending of the number of arguments passed:
* If no arguments are passed to the script, print `No argument`
* If only one argument is passed to the script, print `Argument found`
* Otherwise, print `Arguments found`
* You must use `console.log(...)` to print all output
* You are not allowed to use var

Reference: [`process.argv`](https://nodejs.org/api/process.html#process_process_argv)

File(s): [`2-arguments.js`](./2-arguments.js)

### :white_check_mark: 3. Value of my argument
Write a script that prints the first argument passed to it:
* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

File(s): [`3-value_argument.js`](./3-value_argument.js)

### :white_check_mark: 4. Create a sentence
Write a script that prints two arguments passed to it, in the following format: ` is `
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File(s): [`4-concat.js`](./4-concat.js)

### :white_check_mark: 5. An Integer
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
* If the argument can’t be converted to an integer, print `Not a number`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try`/`catch`

File(s): [`5-to_integer.js`](./5-to_integer.js)

### :white_check_mark: 6. Loop to languages
Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop
* The first line: `C is fun`
* The second line: `Python is cool`
* The third line: `JavaScript is amazing`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if`/`else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

File(s): [`6-multi_languages_loop.js`](./6-multi_languages_loop.js)

### :white_check_mark: 7. I love C
Write a script that prints x times `C is fun`
* Where `x` is the first argument of the script
* If the first argument can’t be converted to an integer, print `Missing number of occurrences`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only two `console.log`
* You must use a loop (`while`, `for`, etc.)

File(s): [`7-multi_c.js`](./7-multi_c.js)

### :white_check_mark: 8. Square
Write a script that prints a square
* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

File(s): [`8-square.js`](./8-square.js)

### :white_check_mark: 9. Add
Write a script that prints the addition of 2 integers
* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File(s): [`9-add.js`](./9-add.js)

### :white_check_mark: 10. Factorial
Write a script that computes and prints a factorial
* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* You must do it recursively
* You must use a function
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File(s): [`10-factorial.js`](./10-factorial.js)

### :white_check_mark: 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.
* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

File(s): [`11-second_biggest.js`](./11-second_biggest.js)

### :white_check_mark: 12. Object
Update the provided script `12-object.js` to replace the value 12 with 89:
* You are not allowed to use `var`

File(s): [`12-object.js`](./12-object.js)

### :white_check_mark: 13. Add file
Write a function that returns the addition of 2 integers.
* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`

[Tip](https://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

File(s): [`13-add.js`](./13-add.js)

## Advanced Tasks

### :white_check_mark: 14. Const or not const
Write a file that modifies the value of `myVar` to `333` when running [`100-main.js`](./tests/100-main.js)

Hint: scope

Note: this exercise doesn’t pass the `semistandard` linter.

File(s): [`100-let_me_const.js`](./100-let_me_const.js)

### :white_check_mark: 15. Call me Moby
Write a function that executes a function `x` times.
* The function must be visible from outside
* Prototype: `function (x, theFunction)`
* You are not allowed to use `var`

File(s): [`101-call_me_moby.js`](./101-call_me_moby.js)

### :white_check_mark: 16. Add me maybe
Write a function that increments and calls a function.
* The function must be visible from outside
* Prototype: `function (number, theFunction)`
* You are not allowed to use `var`

File(s): [`102-add_me_maybe.js`](./102-add_me_maybe.js)

### :white_check_mark: 17. Increment object
Update the provided script `103-object_fct.js` by adding a new function `incr` that increments the integer `vaslue`.
* You are not allowed to use `var`

File(s): [`103-object_fct.js`](./103-object_fct.js)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
