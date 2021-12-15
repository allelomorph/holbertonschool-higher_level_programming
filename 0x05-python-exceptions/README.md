# (245) 0x05. Python - Exceptions
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
05-18-2020 to 05-19-2020

### Description
Introduction to exceptions: raising, catching, and when best employed.

### Provided file(s)
* [`0-main.py`](./tests/0-main.py)  [`1-main.py`](./tests/1-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-main.py`](./tests/6-main.py) [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py)
* [`103-tests.py`](./tests/103-tests.py)

---

## Mandatory Tasks

### :white_check_mark: 0. Safe list printing
Write a function that prints x elements of a list.
* Prototype: `def safe_print_list(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All elements must be printed on the same line followed by a new line.
* `x` represents the number of elements to print
* `x` can be bigger than the length of `my_list`
* Returns the real number of elements printed
* You have to use `try:` / `except:`
* You are not allowed to import any module
* You are not allowed to use `len()`

File(s): [`0-safe_print_list.py`](./0-safe_print_list.py)

### :white_check_mark: 1. Safe printing of an integers list
Write a function that prints an integer with `"{:d}".format()`.
* Prototype: `def safe_print_integer(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if value has been correctly printed (it means the value is an integer)
* Otherwise, returns `False`
* You have to use `try:` / `except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to import any module
* You are not allowed to use `type()`

File(s): [`1-safe_print_integer.py`](./1-safe_print_integer.py)

### :white_check_mark: 2. Print and count integers
Write a function that prints the first `x` elements of a list and only integers.
* Prototype: `def safe_print_list_integers(my_list=[], x=0):`
* `my_list` can contain any type (integer, string, etc.)
* All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
* `x` represents the number of elements to access in `my_list`
* `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
* Returns the real number of integers printed
* You have to use `try:` / `except:`
* You have to use `"{:d}".format()` to print an integer
* You are not allowed to import any module
* You are not allowed to use `len()`

File(s): [`2-safe_print_list_integers.py`](./2-safe_print_list_integers.py)

### :white_check_mark: 3. Integers division with debug
Write a function that divides 2 integers and prints the result.
* Prototype: `def safe_print_division(a, b):`
* You can assume that `a` and `b` are integers
* The result of the division should print on the `finally:` section preceded by `Inside result:`
* Returns the value of the division, otherwise: `None`
* You have to use `try:` / `except:` / `finally:`
* You have to use `"{}".format()` to print the result
* You are not allowed to import any module

File(s): [`3-safe_print_division.py`](./3-safe_print_division.py)

### :white_check_mark: 4. Divide a list
Write a function that divides element by element 2 lists.
* Prototype: `def list_division(my_list_1, my_list_2, list_length):`
* `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
* `list_length` can be bigger than the length of both lists
* Returns a new list (length = `list_length`) with all divisions
* If 2 elements can’t be divided, the division result should be equal to 0
* If an element is not an integer or float:
    * print: `wrong type`
* If the division can’t be done (/0):
    * print: `division by 0`
* If `my_list_1` or `my_list_2` is too short
    * print: `out of range`
* You have to use `try:` / `except:` / `finally:`
* You are not allowed to import any module

File(s): [`4-list_division.py`](./4-list_division.py)

### :white_check_mark: 5. Raise exception
Write a function that raises a type exception.
* Prototype: `def raise_exception():`
* You are not allowed to import any module

File(s): [`5-raise_exception.py`](./5-raise_exception.py)

### :white_check_mark: 6. Raise a message
Write a function that raises a name exception with a message.
* Prototype: `def raise_exception_msg(message=""):`
* You are not allowed to import any module

File(s): [`6-raise_exception_msg.py`](./6-raise_exception_msg.py)

## Advanced Tasks

### :white_check_mark: 7. Safe integer print with error message
Write a function that prints an integer.
* Prototype: `def safe_print_integer_err(value):`
* `value` can be any type (integer, string, etc.)
* The integer should be printed followed by a new line
* Returns `True` if value has been correctly printed (it means the value is an integer)
* Otherwise, returns `False` and prints in `stderr` the error precede by `Exception:`
* You have to use `try:` / `except:`
* You have to use `"{:d}".format()` to print as integer
* You are not allowed to use `type()`

File(s): [`100-safe_print_integer_err.py`](./100-safe_print_integer_err.py)

### :white_check_mark: 8. Safe function
Write a function that executes a function safely.
* Prototype: `def safe_function(fct, *args):`
* You can assume `fct` will be always a pointer to a function
* Returns the result of the function,
* Otherwise, returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`
* You have to use `try:` / `except:`

File(s): [`101-safe_function.py`](./101-safe_function.py)

### :white_check_mark: 9. ByteCode -> Python #4
Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
* Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

File(s): [`102-magic_calculation.py`](./102-magic_calculation.py)

### :white_large_square: 3. CPython #2: PyFloatObject
Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.

Python lists:
* Prototype: `void print_python_list(PyObject *p);`
* If `p` is not a valid `PyListObject`, print an error message

Python bytes:
* Prototype: `void print_python_bytes(PyObject *p);`
* Line “first X bytes”: print a maximum of 10 bytes
* If `p` is not a valid `PyBytesObject`, print an error message

Python float:
* Prototype: `void print_python_float(PyObject *p);`
* If `p` is not a valid `PyFloatObject`, print an error message
* Read `/usr/include/python3.4/floatobject.h`

About:
* Python version: 3.4
* You are allowed to use the C standard library
* Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
* You are not allowed to use the following macros/functions:
    * `Py_SIZE`
    * `Py_TYPE`
    * `PyList_Size`
    * `PyList_GetItem`
    * `PyBytes_AS_STRING`
    * `PyBytes_GET_SIZE`
    * `PyBytes_AsString`
    * `PyFloat_AS_DOUBLE`
    * `PySequence_GetItem`
    * `PySequence_Fast_GET_SIZE`
    * `PySequence_Fast_GET_ITEM`
    * `PySequence_ITEM`
    * `PySequence_Fast_ITEMS`

**NOTE:**
* The Python script will be launched using the `-u` option (force stdout to be unbuffered).
* It is **strongly** advised to either use `setbuf(stdout, NULL);` or `fflush(stdout)` in your C functions IF you choose to use printf. The reason to that is that Python's `print` and libC's `printf` don’t share the same buffer, and the output can appear disordered.

File(s): [`1033-python.c`](./103-python.c)\
Compiled: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 3-python.c`

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
