# holbertonschool-higher_level_programming

## Description
High level / OOP component of the Holberton school core curriculum, with a focus on the basics of Python programming, plus an introduction to SQL and Javascript. 

## General requirements

### bash
* Interpreter conditions:
  * Ubuntu 14.04 LTS
* First line of executable scripts wiil be `#!/bin/bash`

### C
* Compilation conditions:
  * Ubuntu 14.04 LTS
  * gcc 4.8.4
  * flags `-Wall -Werror -Wextra -pedantic`
* Compliance with linters:
  * [betty-style](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl)
  * [betty-doc](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
* Test mains will typically not be in same directory as the task solutions, add `-I.` to `gcc` flags to allow test mains to include headers from main directory

### Python
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * python3 (version 3.4.3)
* First line of executable scripts wiil be `#!/usr/bin/python3`
* Compliance with linter:
  * `pep8` (version 1.7.*) (now known as `pycodestyle`)
* Docstrings are expected to follow the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html):
  * Per module (`python3 -c 'print(__import__("my_module").__doc__)'`)
  * Per class (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  * Per function (both inside and outside a class) (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* Test scripts will typically not be in same directory as the task solutions, use `export PYTHONPATH='.'` before running test scripts from project directory to allow includes

### Javascript
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * Node 10.x
    * with `request` module
* First line of executable scripts wiil be `#!/usr/bin/node`
* Compliance with linter:
  * `semistandard` (version 16.0.*)

---

### [(231) 0x00. Python - Hello, World](./0x00-python-hello_world/)
First introduction to scripting in Python 3, and basic use of strings.

### [(233) 0x01. Python - if/else, loops, functions](./0x01-python-if_else_loops_functions/)
Introduction to functions and basic flow control in Python.

### [(239) 0x02. Python - import & modules](./0x02-python-import_modules/)
Introduction to how Python source files can reference one another through the use of `import`.

### [(241) 0x03. Python - Data Structures: Lists, Tuples](./0x03-python-data_structures/)
Introduction to the use of lists and tuples: indexing and methods, list comprehensions, sequences, and `del`.

### [(243) 0x04. Python - More Data Structures: Set, Dictionary](./0x04-python-more_data_structures/)
Introduction to the use of sets and dictionaries, how they differ from lists, iteration, key-value pairs, and lambda functions.

### [(245) 0x05. Python - Exceptions](./0x05-python-exceptions/)
Introduction to exceptions: raising, catching, and when best employed.

### [(247) 0x06. Python - Classes and Objects](./0x06-python-classes/)
Introducing Object-Oriented Programming, and how Python's implementation teaches about the concept more broadly.

### [(246) 0x07. Python - Test-driven development](./0x07-python-test_driven_development/)
Introduction to how to create and use a battery of tests, implement tests inside docstrings, and finding edge cases.

### [(250) 0x08. Python - More Classes and Objects](./0x08-python-more_classes/)
Further exploration of Object-Oriented Programming concepts as represented in Python, such as attributes (class vs instance,) and methods (class vs static, getters vs setters, `__init__`, `__str__`, `__repr__`.)

### [(252) 0x09. Python - Everything is object](./0x09-python-everything_is_object/)
Investigating the mutability of objects in Python, comparing classes vs objects vs instances, and reference vs assignment vs aliases.

### [(254) 0x0A. Python - Inheritance](./0x0A-python-inheritance/)
How one class can be derived from another, how attributes and methods of a parent class are accessible by the child, plus the use of relevant built-in Python methods like `isinstance` and `issubclass`.

### [(260) 0x0B. Python - Input/Output](./0x0B-python-input_output/)
Introduction to reading from and writing to files in Python, and serialization/deserialization using the JSON format.

### [0x0C. Python - Almost a circle](./0x0C-python-almost_a_circle/)


### [0x0D. SQL - Introduction](./0x0D-SQL_introduction/)


### [0x0E. SQL - More queries](./0x0E-SQL_more_queries/)


### [0x0F. Python - Object-relational mapping](./0x0F-python-object_relational_mapping/)


### [0x10. Python - Network #0](./0x10-python-network_0/)


### [0x11. Python - Network #1](./0x11-python-network_1/)


### [0x12. Javascript - Warm up](./0x12-javascript-warm_up/)


### [0x13. Javascript - Objects, Scopes and Closures](./0x13-javascript_objects_scopes_closures/)


### [0x14. JavaScript - Web scraping](./0x14-javascript-web_scraping/)


### [0x15. Javascript - Web JQuery](./0x15-javascript-web_jquery/)


---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)