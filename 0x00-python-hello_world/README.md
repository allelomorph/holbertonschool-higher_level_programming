# (231) 0x00. Python - Hello, World
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
04-27-2020 to 04-28-2020

### Description
First introduction to scripting in Python 3, and basic use of strings.

### Provided file(s)
* [`main.py`](./tests/main.py)
* original incomplete versions of [`3-print_number.py`](./3-print_number.py) [`4-print_float.py`](./4-print_float.py) [`5-print_string.py`](./5-print_string.py) [`6-concat.py`](./6-concat.py) [`7-edges.py`](./7-edges.py) [`8-concat_edges.py`](./8-concat_edges.py)
* [`lists.h`](./lists.h) [`10-linked_lists.c`](./10-linked_lists.c)

---

## Mandatory Tasks

### :white_check_mark: 0. Run Python file
Write a Shell script that runs a Python script.\
The Python file name will be saved in the environment variable `$PYFILE`

File(s): [`0-run`](./0-run)

### :white_check_mark: 1. Run inline
Write a Shell script that runs Python code.\
The Python code will be saved in the environment variable `$PYCODE`

File(s): [`1-run_inline`](./1-run_inline)

### :white_check_mark: 2. Hello, print
Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
* Use the function `print`

File(s): [`2-print.py`](./2-print.py)

### :white_check_mark: 3. Print integer
Complete the provided source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
* You are not allowed to cast the variable number into a string
* Your code must be 3 lines long
* You have to use the [new style](https://pyformat.info/#number) of printing numbers (with `.format(...)`)

File(s): [`3-print_number.py`](./3-print_number.py)

### :white_check_mark: 4. Print float
Complete the provided source code in order to print the float stored in the variable `number` with a precision of 2 digits.
* The output of the program should be:
    * `Float:`, followed by the float with only 2 digits
    * followed by a new line
* You are not allowed to cast `number` to string
* You have to use the [new style](https://pyformat.info/#number) of printing numbers (with `.format(...)`)

File(s): [`4-print_float.py`](./4-print_float.py)

### :white_check_mark: 5. Print string
Complete the provided source code in order to print a string stored in the variable str 3 times, followed by its first 9 characters.
* The output of the program should be:
    * 3 times the value of `str`
    * followed by a new line
    * followed by the 9 first characters of `str`
    * followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long

File(s): [`5-print_string.py`](./5-print_string.py)

### :white_check_mark: 6. Play with strings
Complete the provided source code to print `Welcome to Holberton School!`
* You are not allowed to use any loops or conditional statements
* You have to use the variables `str1` and `str2` in your new line of code
* Your program should be exactly 5 lines long

File(s): [`6-concat.py`](./6-concat.py)

### :white_check_mark: 7. Copy - Cut - Paste
Complete the provided source code
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable `word`
* `word_last_2` should contain the last 2 letters of the variable `word`
* `middle_word` should contain the value of the variable word without the first and last letters

File(s): [`7-edges.py`](./7-edges.py)

### :white_check_mark: 8. Create a new sentence
Complete the provided source code to print object-oriented programming with Python, followed by a new line.
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals

File(s): [`8-concat_edges.py`](./8-concat_edges.py)

### :white_check_mark: 9. Easter Egg
Write a Python script that prints “The Zen of Python”, by Tim Peters, followed by a new line.
* Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

File(s): [`9-easter_egg.py`](./9-easter_egg.py)

### :white_check_mark: 10. Linked list cycle
Write a function in C that checks if a singly linked list has a cycle in it.
* Prototype: `int check_cycle(listint_t *list);`
* Return: 0 if there is no cycle, 1 if there is a cycle

Requirements:
* Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`

File(s): [`10-check_cycle.c`](./10-check_cycle.c)
Compiled: `gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`

## Advanced Tasks

### :white_check_mark: 11. Hello, write
Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
* Use the function `write` from the `sys` module
* You are not allowed to use `print`
* Your script should print to `stderr`
* Your script should exit with the status code 1

File(s): [`100-write.py`](./100-write.py)

### :white_large_square: 12. Compile
Write a script that compiles a Python script file.\
The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

```bash
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./101-compile
Compiling main.py ...
$ ls
101-compile  main.py  main.pyc
$ cat main.pyc | zgrep -c "Best School"
1
$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
$ 
```

File(s): [`101-compile`](./101-compile)

### :white_check_mark: 13. ByteCode -> Python #1
Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
* Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

File(s): [`102-magic_calculation.py`](./102-magic_calculation.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
