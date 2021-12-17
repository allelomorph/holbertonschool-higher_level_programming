# (254) 0x0A. Python - Inheritance
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
06-02-2020 to 06-03-2020

### Description
How one class can be derived from another, how attributes and methods of a parent class are accessible by the child, plus the use of relevant built-in Python methods like `isinstance` and `issubclass`.

### Provided file(s)
* [`0-main.py`](./tests/0-main.py) [`1-main.py`](./tests/1-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-main.py`](./tests/6-main.py) [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py) [`9-main.py`](./tests/9-main.py) [`10-main.py`](./tests/10-main.py)
* [`100-main.py`](./tests/100-main.py) [`101-main.py`](./tests/101-main.py)

---

## Mandatory Tasks

### :white_check_mark: 0. Lookup
Write a function that returns the list of available attributes and methods of an object:
* Prototype: `def lookup(obj):`
* Returns a `list` object
* You are not allowed to import any module

File(s): [`0-lookup.py`](./0-lookup.py)

### :white_check_mark: 1. My list
Write a class `MyList` that inherits from list:
* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`
* You are not allowed to import any module

File(s): [`1-my_list.py`](./1-my_list.py) [`tests/1-my_list.txt`](./tests/1-my_list.txt)

### :white_check_mark: 2. Exact same object
Write a function that returns `True` if the object is *exactly* an instance of the specified class, otherwise `False`.
* Prototype: `def is_same_class(obj, a_class):`
* You are not allowed to import any module

File(s): [`2-is_same_class.py`](./2-is_same_class.py)

### :white_check_mark: 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.
* Prototype: `def is_kind_of_class(obj, a_class):`
* You are not allowed to import any module

File(s): [`3-is_kind_of_class.py`](./3-is_kind_of_class.py)

### :white_check_mark: 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.
* Prototype: `def inherits_from(obj, a_class):`
* You are not allowed to import any module

File(s): [`4-inherits_from.py`](./4-inherits_from.py)

### :white_check_mark: 5. Geometry module
Write an empty class `BaseGeometry`.
* You are not allowed to import any module

File(s): [`5-base_geometry.py`](./5-base_geometry.py)

### :white_check_mark: 6. Improve Geometry
Write a class `BaseGeometry`, based on `5-base_geometry.py`, which adds the following:
* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
* You are not allowed to import any module

File(s): [`6-base_geometry.py`](./6-base_geometry.py)

### :white_check_mark: 7. Integer validator
Write a class `BaseGeometry`, based on `6-base_geometry.py`, which adds the following:
* Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    * you can assume `name` is always a string
    * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
* You are not allowed to import any module

File(s): [`7-base_geometry.py`](./7-base_geometry.py) [`tests/7-base_geometry.txt`](./tests/7-base_geometry.txt)

### :white_check_mark: 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`.)
* Instantiation with `width` and `height`: `def __init__(self, width, height):`
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers, validated by `integer_validator`

File(s): [`8-rectangle.py`](./8-rectangle.py)

### :white_check_mark: 9. Full rectangle
Write a class `Rectangle`, based on `8-rectangle.py`, that inherits from `BaseGeometry` (`7-base_geometry.py,) and adds the following: 
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

File(s): [`9-rectangle.py`](./9-rectangle.py)

### :white_check_mark: 10. Square #1
Write a class Square that inherits from Rectangle (`9-rectangle.py`):
* Instantiation with `size`: `def __init__(self, size):`
    * `size` must be private. No getter or setter
    * `size` must be a positive integer, validated by `integer_validator`
* the `area()` method must be implemented

File(s): [`10-square.py`](./10-square.py)

### :white_check_mark: 11. Square #2
Write a class `Square`, based on `10-square.py`, that inherits from `Rectangle` (`9-rectangle.py`,) and adds the following:
* `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

File(s): [`11-square.py`](./11-square.py)

## Advanced Tasks

### :white_check_mark: 12. My integer
Write a class `MyInt` that inherits from `int`:
* `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
* You are not allowed to import any module

File(s): [`100-my_int.py`](./100-my_int.py)

### :white_check_mark: 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:
* Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
* You are not allowed to use `try`/`catch`
* You are not allowed to import any module

File(s): [`101-add_attribute.py`](./101-add_attribute.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
