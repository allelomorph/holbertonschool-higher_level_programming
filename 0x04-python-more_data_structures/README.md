# (243) 0x04. Python - More Data Structures: Set, Dictionary
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
05-07-2020 to 05-08-2020

### Description
Introduction to the use of sets and dictionaries, how they differ from lists, iteration, key-value pairs, and lambda functions.

### Provided file(s)
* [`0-main.py`](./tests/0-main.py)  [`1-main.py`](./tests/1-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-main.py`](./tests/6-main.py) [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py) [`9-main.py`](./tests/9-main.py) [`10-main.py`](./tests/10-main.py) [`11-main.py`](./tests/11-main.py) [`12-main.c`](./tests/12-main.c)
* [`100-main.py`](./tests/100-main.py) [`101-main.py`](./tests/101-main.py) [`102-main.py`](./tests/102-main.py) [`103-tests.py`](./tests/103-tests.py)

---

## Mandatory Tasks

### :white_check_mark: 0. Squared simple
Write a function that computes the square value of all integers of a matrix.
* Prototype: `def square_matrix_simple(matrix=[]):`
* matrix is a 2 dimensional array
* Returns a new matrix:
    * Same size as `matrix`
    * Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allowed to use regular loops, `map`, etc.

File(s): [`0-square_matrix_simple.py`](./0-square_matrix_simple.py)

### :white_check_mark: 1. Search and replace
Write a function that replaces all occurrences of an element by another in a new list.
* Prototype: `def search_replace(my_list, search, replace):`
* `my_list` is the initial list
* `search` is the element to replace in the list
* `replace` is the new element
* You are not allowed to import any module

File(s): [`1-search_replace.py`](./1-search_replace.py)

### :white_check_mark: 2. Unique addition
Write a function that adds all unique integers in a list (only once for each integer).
* Prototype: `def uniq_add(my_list=[]):`
* You are not allowed to import any module

File(s): [`2-uniq_add.py`](./2-uniq_add.py)

### :white_check_mark: 3. Present in both
Write a function that returns a set of common elements in two sets.
* Prototype: `def common_elements(set_1, set_2):`
* You are not allowed to import any module

File(s): [`3-common_elements.py`](./3-common_elements.py)

### :white_check_mark: 4. Only differents
Write a function that returns a set of all elements present in only one set.
* Prototype: `def only_diff_elements(set_1, set_2):`
* You are not allowed to import any module

File(s): [`4-only_diff_elements.py`](./4-only_diff_elements.py)

### :white_check_mark: 5. Number of keys
Write a function that returns the number of keys in a dictionary.
* Prototype: `def number_keys(a_dictionary):`
* You are not allowed to import any module

File(s): [`5-number_keys.py`](./5-number_keys.py)

### :white_check_mark: 6. Print sorted dictionary
Write a function that prints a dictionary by ordered keys.
* Prototype: `def print_sorted_dictionary(a_dictionary):`
* You can assume that all keys are strings
* Keys should be sorted by alphabetic order
* Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
* Dictionary values can have any type
* You are not allowed to import any module

File(s): [`6-print_sorted_dictionary.py`](./6-print_sorted_dictionary.py)

### :white_check_mark: 7. Update dictionary
Write a function that replaces or adds key/value in a dictionary.
* Prototype: `def update_dictionary(a_dictionary, key, value):`
* `key` argument will be always a string
* `value` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* You are not allowed to import any module

File(s): [`7-update_dictionary.py`](./7-update_dictionary.py)

### :white_check_mark: 8. Simple delete by key
Write a function that deletes a key in a dictionary.
* Prototype: `def simple_delete(a_dictionary, key=""):`
* `key` argument will be always a string
* If a key doesn’t exist, the dictionary won’t change
* You are not allowed to import any module

File(s): [`8-simple_delete.py`](./8-simple_delete.py)

### :white_check_mark: 9. Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2
* Prototype: `def multiply_by_2(a_dictionary):`
* You can assume that all values are only integers
* Returns a new dictionary
* You are not allowed to import any module

File(s): [`9-multiply_by_2.py`](./9-multiply_by_2.py)

### :white_check_mark: 10. Best score
Write a function that returns a key with the biggest integer value.
* Prototype: `def best_score(a_dictionary):`
* You can assume that all values are only integers
* If no score found, return `None`
* You can assume all students have a different score
* You are not allowed to import any module

File(s): [`10-best_score.py`](./10-best_score.py)

### :white_check_mark: 11. Multiply by using map
Write a function that returns a list with all values multiplied by a number without using any loops.
* Prototype: `def multiply_list_map(my_list=[], number=0):`
* Returns a new list:
    * Same length as `my_list`
    * Each value should be multiplied by number
* Initial list should not be modified
* You are not allowed to import any module
* You have to use `map`
* Your file should be max 3 lines

File(s): [`11-multiply_list_map.py`](./11-multiply_list_map.py)

### :white_check_mark: 12. Roman to Integer
**Technical interview preparation**:
* You are not allowed to google anything
* Whiteboard first

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.
* You can assume the number will be between 1 to 3999.
* `def roman_to_int(roman_string)` must return an integer
* If the `roman_string` is not a string or `None`, return 0

File(s): [`12-roman_to_int.py`](./12-roman_to_int.py)

## Advanced Tasks

### :white_check_mark: 13. Weighted average!
Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`
* Prototype: `def weight_average(my_list=[]):`
* Returns 0 if the list is empty
* You are not allowed to import any module

File(s): [`100-weight_average.py`](./100-weight_average.py)

### :white_check_mark: 14. Squared by using map
Write a function that computes the square value of all integers of a matrix using map
* Prototype: `def square_matrix_map(matrix=[]):`
* `matrix` is a 2 dimensional array
* Returns a new matrix:
    * Same size as `matrix`
    * Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You have to use `map`
* You are not allowed to use `for` or `while`
* Your file should be max 3 lines

File(s): [`101-square_matrix_map.py`](./101-square_matrix_map.py)

### :white_check_mark: 15. Delete by value
Write a function that deletes keys with a specific value in a dictionary.
* Prototype: `def complex_delete(a_dictionary, value):`
* If the value doesn’t exist, the dictionary won’t change
* All keys having the searched value have to be deleted
* You are not allowed to import any module

File(s): [`102-complex_delete.py`](./102-complex_delete.py)

### :white_large_square: 16. CPython #1: PyBytesObject
Create two C functions that print some basic info about Python lists and Python bytes objects.

Python lists:
* Prototype: `void print_python_list(PyObject *p);`

Python bytes:
* Prototype: `void print_python_bytes(PyObject *p);`
* Line “first X bytes”: print a maximum of 10 bytes
* If `p` is not a valid `PyBytesObject`, print an error message (see example)
* Read `/usr/include/python3.4/bytesobject.h`

About:
* Python version: 3.4
* Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
* You are not allowed to use the following macros/functions:
    * `Py_SIZE`
    * `Py_TYPE`
    * `PyList_GetItem`
    * `PyBytes_AS_STRING`
    * `PyBytes_GET_SIZE`

File(s): [`103-python.c`](./103-python.c)\
Compiled: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
