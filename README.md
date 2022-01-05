# holbertonschool-higher_level_programming

## Description
Object-oriented programming component of the Holberton school core curriculum, with a focus on the basics of Python, plus an introduction to SQL databases and Javascript.

## Note
Also considered part of this track is the [AirBnB clone project arc](#airbnb-clone), which combines many of the skills learned in this track along with those from the [System Engineering and DevOps track](https://github.com/allelomorph/holberton-system_engineering-devops) to create a fully functional website with its own back end console and database storage.

Four iterations of the project were produced, each in its own separate repository. See [AirBnB clone section](#airbnb-clone) for a list of relevant assignment overiews linked from each repository.

## General requirements

### bash
* Interpreter conditions:
  * Ubuntu 14.04 LTS
* First line of executable scripts will be `#!/bin/bash`

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
* First line of executable scripts will be `#!/usr/bin/python3`
* Compliance with linter:
  * `pep8` (version 1.7.*) (now known as `pycodestyle`)
* Docstrings are expected to follow the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html):
  * Per module (`python3 -c 'print(__import__("my_module").__doc__)'`)
  * Per class (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  * Per function
    * both inside a class (`python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
    * and outside a class (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* Test scripts will typically not be in same directory as the task solutions, use `export PYTHONPATH='.'` before running test scripts from project directory to allow includes
* Unit tests will be required on some projects:
  * using the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
  * located in a `tests/` folder, with a file structure mimicing that of your project, but with a `test_` prefix added to all file/directory names
  * tests should be capable of being run with `python3 -m unittest discover tests`, or individually per file with `python3 -m unittest <test file>`

### SQL
* `.sql` file comments prefixed with `-- `
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * mysql Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using EditLine wrapper

### Use of MySQL
* `sudo apt install mysql-server` to install
* Interactive mode with `sudo mysql`, non-interactive with:
```bash
$ service mysql start
$ cat <script> | mysql -uroot -p
```
* Import a SQL dump:
```bash
$ echo "CREATE DATABASE <database>;" | mysql -uroot -p
$ curl <dump_file_uri> -s | mysql -uroot -p <database>
```

### Javascript
* Interpreter conditions:
  * Ubuntu 14.04 LTS
  * Node 10.x
    * with `request` module
* First line of executable scripts wiil be `#!/usr/bin/node`
* Compliance with linter:
  * `semistandard` (version 16.0.*)
  * standards references:
    * [JavScript Standard Rules](https://standardjs.com/rules.html)
    * [`semistandard` documentation](https://github.com/standard/semistandard)
    * [AirBnB JavaScript standard](https://github.com/airbnb/javascript)

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

### [(331) 0x0C. Python - Almost a circle](./0x0C-python-almost_a_circle/)
In preparation for the AirBnB clone project cycle, a review of all Python concepts covered so far: importing, exceptions, classes, private attributes, getter/setters, class/static methods, inheritance, unit testing, file I/O, and JSON serialization. In addition, `args` and `kwargs` are introduced.

### [(272) 0x0D. SQL - Introduction](./0x0D-SQL_introduction/)
Introduction to database storage via MySQL and creating SQL queries and functions.

### [(274) 0x0E. SQL - More queries](./0x0E-SQL_more_queries/)
Addtional database and SQL concepts: managing user privileges, `PRIMARY KEY`/`FOREIGN KEY`, querying multiple tables, `JOIN`s and `UNION`s. 

### [(283) 0x0F. Python - Object-relational mapping](./0x0F-python-object_relational_mapping/)
Bridging the gap between Python and SQL in two ways: using the module `MySQLdb` to connect to a database and execute SQL queries, and using the `SQLAlchemy` module as an introduction to Object Relational Mapping.

### [(299) 0x10. Python - Network #0](./0x10-python-network_0/)
Introduction to the basics of HTTP requests and responses, URLs and their components, and using `curl` from the command line.

### [(300) 0x11. Python - Network #1](./0x11-python-network_1/)
Continued exploration of the Pythonic approach to HTTP requests and responses, this time using the `urllib` and `requests` packages.

### [(303) 0x12. Javascript - Warm up](./0x12-javascript-warm_up/)
A simple introduction to JavaScript, when used as a scripting language and for web front-end.

### [(304) 0x13. Javascript - Objects, Scopes and Closures](./0x13-javascript_objects_scopes_closures/)
Introduction to Object-Oriented Programming in JavaScript: objects, classes, inheritance, scope, closure, `this`, and `undefined`.

### [(333) 0x14. JavaScript - Web scraping](./0x14-javascript-web_scraping/)
Pulling JSON data from the web using JavaScript's `request` module and Fetch API to make HTTP requests, plus file I/O with the `fs` module.

### [(305) 0x15. Javascript - Web JQuery](./0x15-javascript-web_jquery/)
Using JavaScript and JQuery to get and modify HTML, JQuery Ajax to handle HTTP requests, and JavaScript to listen and bind to user or DOM events.

---

## AirBnB clone

### [(263) 0x00. AirBnB clone - The console](https://github.com/allelomorph/AirBnB_clone/blob/master/PROJECT_0x00.md)
Review of concepts like unit testing, JSON serialization/deserialization, and `*args`/`**kwargs` in Python, plus an introduction to UUIDs and the `cmd` module. Creating a command line interpreter to store data objects in local JSON files.

### [(268) 0x01. AirBnB clone - Web static](https://github.com/allelomorph/AirBnB_clone/blob/master/PROJECT_0x01.md)
Introduction to HTML (elements, tags, and attributes) and CSS (classes, selectors, specificity, box properties.) Establishing style choices in a static web page which will serve as a framework for dynamic content in later versions.

### [(289) 0x02. AirBnB clone - MySQL](https://github.com/allelomorph/AirBnB_clone_v2/blob/master/PROJECT_0x02.md)
Review of Object Relational Mapping. Building a MySQL database as a second storage engine accessible from our back end Python console.

### [(288) 0x03. AirBnB clone - Deploy static](https://github.com/allelomorph/AirBnB_clone_v2/blob/master/PROJECT_0x03.md)
Revisiting Continuous Integration/Continuous Deployment and Nginx concepts from [`holberton-system_engineering-devops`](https://github.com/allelomorph/holberton-system_engineering-devops), plus an intrduction to the Python library Fabric. Deploying the static web content from [(268) 0x01. AirBnB clone - Web static](https://github.com/allelomorph/AirBnB_clone/blob/master/PROJECT_0x01.md) to a simple architecture of two web servers and one load balancer.

### [(290) 0x04. AirBnB clone - Web framework](https://github.com/allelomorph/AirBnB_clone_v2/blob/master/PROJECT_0x04.md)
Using the Python library Flask along with Jinja templates to create a web application to dynamically display the contents of our storage engines.

### [(301) 0x05. AirBnB clone - RESTful API](https://github.com/allelomorph/AirBnB_clone_v3/blob/master/PROJECT_0x05.md)
Using Flask in Python to create an API that can query the storage engine and serve JSON reponses.

### [(309) 0x06. AirBnB clone - Web dynamic](https://github.com/allelomorph/AirBnB_clone_v4/blob/master/PROJECT_0x06.md)
Serving dynamically generated HTML content by querying the API built in the previous iteration using JQuery Ajax. Listening and binding to user or DOM events.

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)