# (250) 0x08. Python - More Classes and Objects
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
05-22-2020 to 05-27-2020

### Description
Further exploration of Object-Oriented Programming concepts as represented in Python, such as attributes (class vs instance,) and methods (class vs static, getters vs setters, `__init__`, `__str__`, `__repr__`.)

### Provided file(s)
* [`0-main.py`](./tests/0-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-main.py`](./tests/6-main.py) [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py) [`9-main.py`](./tests/9-main.py)

---

## Mandatory Tasks

### :white_check_mark: 0. Simple rectangle
Write an empty class `Rectangle` that defines a rectangle:
    You are not allowed to import any module

File(s): [`0-rectangle.py`](./0-rectangle.py)

### :white_check_mark: 1. Real definition of a rectangle
Write a class `Rectangle`, based on `0-rectangle.py`, that defines a rectangle by:
    Private instance attribute: `width`:
        property `def width(self):` to retrieve it
        property setter `def width(self, value):` to set it:
            `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
            if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
    Private instance attribute: `height`:
        property `def height(self):` to retrieve it
        property setter `def height(self, value):` to set it:
            `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
            if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
    Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
    You are not allowed to import any module

File(s): [`1-rectangle.py`](./1-rectangle.py)

### :white_check_mark: 2. Area and Perimeter
Write a class `Rectangle`, based on `1-rectangle.py`, that adds the following:
    Public instance method: `def area(self):` that returns the rectangle area
    Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to 0, perimeter is equal to 0
    You are not allowed to import any module

File(s): [`2-rectangle.py`](./2-rectangle.py)

### :white_check_mark: 3. String representation
Write a class `Rectangle`, based on `2-rectangle.py`, that adds the following:
    `print()` and `str()` should print the rectangle with the character `#`:
        if `width` or `height` is equal to 0, return an empty string
    You are not allowed to import any module

File(s): [`3-rectangle.py`](./3-rectangle.py)

### :white_check_mark: 4. Eval is magic
Write a class `Rectangle`, based on `3-rectangle.py`, that adds the following:
    `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
    You are not allowed to import any module

File(s): [`4-rectangle.py`](./4-rectangle.py)

### :white_check_mark: 5. Detect instance deletion
Write a class `Rectangle`, based on `4-rectangle.py`, that adds the following:
    Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted
    You are not allowed to import any module

File(s): [`5-rectangle.py`](./5-rectangle.py)

### :white_check_mark: 6. How many instances
Write a class `Rectangle`, based on `5-rectangle.py`, that adds the following:
    Public class attribute `number_of_instances`:
        Initialized to 0
        Incremented during each new instance instantiation
        Decremented during each instance deletion
    You are not allowed to import any module

File(s): [`6-rectangle.py`](./6-rectangle.py)

### :white_check_mark: 7. Change representation
Write a class `Rectangle`, based on `6-rectangle.py`, that adds the following:
    Public class attribute `print_symbol`:
        Initialized to `#`
        Used as symbol for string representation
        Can be any type
    You are not allowed to import any module

File(s): [`7-rectangle.py`](./7-rectangle.py)

### :white_check_mark: 8. Compare rectangles
Write a class `Rectangle`, based on `7-rectangle.py`, that adds the following:
    Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
        `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
        `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
    Returns `rect_1` if both have the same area value
    You are not allowed to import any module

File(s): [`8-rectangle.py`](./8-rectangle.py)

### :white_check_mark: 9. A square is a rectangle
    Class method `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`
    You are not allowed to import any module

File(s): [`9-rectangle.py`](./9-rectangle.py)

## Advanced Tasks

### :white_large_square: 10. Class and instance attributes
Write a blog post describing how object and class attributes work.
    What’s a class attribute
    What’s an instance attribute
    What are all the ways to create them and what is the Pythonic way of doing it
    What are the differences between class and instance attributes
    What are the advantages and drawbacks of each of them
    How does Python deal with the object and class attributes using the `__dict__`

Your posts should have examples and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

### :white_check_mark: 11. N queens
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
    Usage: `nqueens N`
        If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
        If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
	Solutions printed as lists of lists of coordinate pairs
        You don’t have to print the solutions in a specific order
    You are only allowed to import the `sys` module

Read: [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

File(s): [`101-nqueens.py`](./101-nqueens.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
