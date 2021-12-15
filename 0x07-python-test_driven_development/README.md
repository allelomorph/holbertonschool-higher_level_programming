# (246) 0x07. Python - Test-driven development
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
05-21-2020 to 05-23-2020

### Description
Introduction to how to create and use a battery of tests, implement tests inside docstrings, and finding edge cases.

### Provided file(s)
* [`0-main.py`](./tests/0-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-max_integer.py`](./tests/6-max_integer.py)
* [`100-main.py`](./tests/100-main.py) [`101-main.py`](./tests/101-main.py) [`102-tests.py`](./tests/102-tests.py)

### Note
Error in project formatting scheme advances file numbering +1 for every task after 0. No ``1-*.py`` or ``1-*.txt`` files as a result.

---

## Mandatory Tasks

### :white_check_mark: 0. Integers addition
Write a function that adds 2 integers.
* Prototype: `def add_integer(a, b=98):`
* `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer or b must be an integer`
* `a` and `b` must be first casted to integers if they are float
* Returns an integer: the addition of `a` and `b`
* You are not allowed to import any module

File(s): [`0-add_integer.py`](./0-add_integer.py) [`tests/0-add_integer.txt`](./tests/0-add_integer.txt)

### :white_check_mark: 1. Divide a matrix
Write a function that divides all elements of a matrix.
* Prototype: `def matrix_divided(matrix, div):`
* `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
* Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
* `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
* `div` can’t be equal to 0, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
* All elements of the matrix should be divided by `div`, rounded to 2 decimal places
* Returns a new matrix
* You are not allowed to import any module

File(s): [`2-matrix_divided.py`](./2-matrix_divided.py) [`tests/2-matrix_divided.txt`](./tests/2-matrix_divided.txt)

### :white_check_mark: 2. Say my name
Write a function that prints `My name is <first name> <last name>`
* Prototype: `def say_my_name(first_name, last_name=""):`
* `first_name` and `last_name` must be strings. Otherwise, raise a `TypeError` exception with the message `first_name must be a string or last_name must be a string`
* You are not allowed to import any module

File(s): [`3-say_my_name.py`](./3-say_my_name.py) [`tests/3-say_my_name.txt`](./tests/3-say_my_name.txt)

### :white_check_mark: 3. Print square
Write a function that prints a square with the character `#`.
* Prototype: `def print_square(size):`
* `size` is the length of the square's side
* `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
* if `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
* if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
* You are not allowed to import any module

File(s): [`4-print_square.py`](./4-print_square.py) [`tests/4-print_square.txt`](./tests/4-print_square.txt)

### :white_check_mark: 4. Text indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
* Prototype: `def text_indentation(text):`
* `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
* There should be no space at the beginning or at the end of each printed line
* You are not allowed to import any module

File(s): [`5-text_indentation.py`](./5-text_indentation.py) [`tests/5-text_indentation.txt`](./tests/5-text_indentation.txt)

### :white_check_mark: 5. Max integer - Unittest
Previous tasks have been concerning “Interactive tests”, now we take a look at unit tests by creating some for the function `def max_integer(list=[]):`.
* Your test file should be inside a folder `tests`
* You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* Your test file should be a python file (extension: `.py`)
* Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`

File(s): [`tests/6-max_integer_test.py`](./tests/6-max_integer_test.py)

## Advanced Tasks

### :white_check_mark: 6. Matrix multiplication
Write a function that multiplies 2 matrices:

* Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)
* Prototype: `def matrix_mul(m_a, m_b):`
* `m_a` and `m_b` must be validated with these requirements in this order
* `m_a` and `m_b` must be an list of lists of integers or floats:
    * if `m_a` or `m_b` is not a list: raise a `TypeError` exception with the message `m_a must be a list` or `m_b must be a list`
    * if `m_a` or `m_b` is not a list of lists: raise a `TypeError` exception with the message `m_a must be a list of lists or m_b must be a list of lists`
    * if `m_a` or `m_b` is empty (it means: = [] or = [[]]): raise a `ValueError` exception with the message `m_a can't be empty or m_b can't be empty`
    * if one element of those list of lists is not an integer or a float: raise a `TypeError` exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`
    * if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raise a `TypeError` exception with the message `each row of m_a must be of the same size or each row of m_b must be of the same size`
* If `m_a` and `m_b` can’t be multiplied: raise a `ValueError` exception with the message `m_a and m_b can't be multiplied`
* You are not allowed to import any module

File(s): [`100-matrix_mul.py`](./100-matrix_mul.py) [`tests/100-matrix_mul.txt`](./tests/100-matrix_mul.txt)

### :white_large_square: 7. Lazy matrix multiplication
Write a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/)\

To install it: `pip3 install numpy==1.15.0`
* Prototype: `def lazy_matrix_mul(m_a, m_b):`
* Test cases should be the same as `100-matrix_mul` but with new exception type/message

File(s): [`101-lazy_matrix_mul.py`](./101-lazy_matrix_mul.py) [`tests/101-lazy_matrix_mul.txt`](./tests/101-lazy_matrix_mul.txt)

### :white_large_square:  4. CPython #3: Python Strings
Create a function that prints Python strings.
* Prototype: `void print_python_string(PyObject *p);`
* If `p` is not a valid string, print an error message
* Read: [Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html)

About:
* Python version: 3.4
* You are allowed to use the C standard library
* Your shared library will be compiled with this command line: `gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

File(s): [`102-python.c`](./102-python.c)\
Compiled: `gcc -Wall -Wextra -pedantic -Werror -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c`

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
