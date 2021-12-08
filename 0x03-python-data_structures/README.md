# (241) 0x03. Python - Data Structures: Lists, Tuples
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
05-05-2020 to 05-06-2020

### Description
Introduction to the use of lists and tuples: indexing and methods, list comprehensions, sequences, and `del`.

### Provided file(s)
* [`0-main.py`](./tests/0-main.py)  [`1-main.py`](./tests/1-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-main.py`](./tests/6-main.py) [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py) [`9-main.py`](./tests/9-main.py) [`10-main.py`](./tests/10-main.py) [`11-main.py`](./tests/11-main.py) [`13-main.c`](./tests/13-main.c) [`100-test_lists.py`](./tests/100-test_lists.py)
* original incomplete version of [`12-switch.py`](./12-switch.py)

---

## Mandatory Tasks

### :white_check_mark: 0. Print a list of integers
Write a function that prints all integers of a list.
* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

File(s): [`0-print_list_integer.py`](./0-print_list_integer.py)

### :white_check_mark: 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.
* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative, the function should return `None`
* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
* You are not allowed to import any module
* You are not allowed to use `try`/`except`

File(s): [`1-element_at.py`](./1-element_at.py)

### :white_check_mark: 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).
* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative, the function should not modify anything, and returns the original list
* If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use `try`/`except`

File(s): [`2-replace_in_list.py`](./2-replace_in_list.py)

### :white_check_mark: 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
* Prototype: `def print_reversed_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

File(s): [`3-print_reversed_list_integer.py`](./3-print_reversed_list_integer.py)

### :white_check_mark: 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
* Prototype: `def new_in_list(my_list, idx, element):`
* If `idx` is negative, the function should return a copy of the original list
* If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
* You are not allowed to import any module
* You are not allowed to use `try`/`except`

File(s): [`4-new_in_list.py`](./4-new_in_list.py)

### :white_check_mark: 5. Can you C me now?
Write a function that removes all characters `c` and `C` from a string.
* Prototype: `def no_c(my_string):`
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use `str.replace()`

File(s): [`5-no_c.py`](./5-no_c.py)

### :white_check_mark: 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.
* Prototype: `def print_matrix_integer(matrix=[[]]):`
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

File(s): [`6-print_matrix_integer.py`](./6-print_matrix_integer.py)

### :white_check_mark: 7. Tuples addition
Write a function that adds 2 tuples.
* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
    * The first element should be the addition of the first element of each argument
    * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value 0 for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

File(s): [`7-add_tuple.py`](./7-add_tuple.py)

### :white_check_mark: 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.
* Prototype: `def multiple_returns(sentence):`
* If the sentence is empty, the first character should be equal to `None`
* You are not allowed to import any module

File(s): [`8-multiple_returns.py`](./8-multiple_returns.py)

### :white_check_mark: 9. Find the max
Write a function that finds the biggest integer of a list.
* Prototype: `def max_integer(my_list=[]):`
* If the list is empty, return `None`
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin `max()`

File(s): [`9-max_integer.py`](./9-max_integer.py)

### :white_check_mark: 10. Only by 2
Write a function that finds all multiples of 2 in a list.
* Prototype: `def divisible_by_2(my_list=[]):`
* Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

File(s): [`10-divisible_by_2.py`](./10-divisible_by_2.py)

### :white_check_mark: 11. Delete at
Write a function that deletes the item at a specific position in a list.
* Prototype: `def delete_at(my_list=[], idx=0):`
* If `idx` is negative or out of range, nothing changes (returns the same list)
* You are not allowed to use `pop()`
* You are not allowed to import any module

File(s): [`11-delete_at.py`](./11-delete_at.py)

### :white_check_mark: 12. Switch
Complete the provided source code in order to switch value of `a` and `b`
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long

File(s): [`12-switch.py`](./12-switch.py)

### :white_check_mark: 13. Linked list palindrome
**Technical interview preparation**:

* You are not allowed to google anything
* Whiteboard first

Write a function in C that checks if a singly linked list is a palindrome.

* Prototype: `int is_palindrome(listint_t **head);`
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
* An empty list is considered a palindrome

File(s): [`13-is_palindrome.c`](./13-is_palindrome.c) [`lists.h`](./lists.h)
Compiled: `gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome`

## Advanced Tasks

### :white_large_square: 14. CPython #0: Python lists
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.

Create a C function that prints some basic info about Python lists.

* Prototype: `void print_python_list(PyObject *p);`
* Python version: 3.4
* Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
* OS: Ubuntu 14.04 LTS
* Start by reading:
    * `listobject.h`
    * `object.h`
    * [Common Object Structures](https://docs.python.org/3.4/c-api/structures.html)
    * [List Objects](https://docs.python.org/3.4/c-api/list.html)

File(s): [`100-print_python_list_info.c`](./100-print_python_list_info.c)\
Compiled: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
