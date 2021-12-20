# (331) 0x0C. Python - Almost a circle
Foundations > Higher-level programming > Python

---

### Project author
Guillaume Salva

### Assignment dates
06-05-2020 to 06-10-2020

### Description
In preparation for the AirBnB clone project cycle, a review of all Python concepts covered so far: importing, exceptions, classes, private attributes, getter/setters, class/static methods, inheritance, unit testing, file I/O, and JSON serialization. In addition, `args` and `kwargs` are introduced.

### Provided file(s)
* [`1-main.py`](./tests/1-main.py) [`2-main.py`](./tests/2-main.py) [`3-main.py`](./tests/3-main.py) [`4-main.py`](./tests/4-main.py) [`5-main.py`](./tests/5-main.py) [`6-main.py`](./tests/6-main.py) [`7-main.py`](./tests/7-main.py) [`8-main.py`](./tests/8-main.py)  [`8-main_2.py`](./tests/8-main_2.py) [`9-main.py`](./tests/9-main.py) [`10-main.py`](./tests/10-main.py) [`11-main.py`](./tests/11-main.py) [`12-main.py`](./tests/12-main.py) [`13-main.py`](./tests/13-main.py) [`14-main.py`](./tests/14-main.py) [`15-main.py`](./tests/15-main.py) [`16-main.py`](./tests/16-main.py) [`17-main.py`](./tests/17-main.py) [`18-main.py`](./tests/18-main.py) [`19-main.py`](./tests/19-main.py)
* [`100-main.py`](./tests/100-main.py) [`101-main.py`](./tests/101-main.py)

---

## Mandatory Tasks

### :white_check_mark: 0. If it's not tested it doesn't work
All your files, classes and methods must be unit tested and be PEP8 (PyCodeStyle) validated.

See [repo README](../) for unit testing requirements.

File(s): [`tests/`](./tests/)

### :white_check_mark: 1. Base class
Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py`:
* Class `Base`:
    * private class attribute `__nb_objects = 0`
    * class constructor: `def __init__(self, id=None):`:
        * if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
        * otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. Its main purpose is to manage an `id` attribute in all its derived classes.

File(s): [`models/base.py`](./models/base.py) [`models/__init__.py`](./models/__init__.py)

### :white_check_mark: 2. First Rectangle
Write the class `Rectangle` that inherits from `Base`:
* Private instance attributes, each with its own public getter and setter:
    * `__width` -> `width`
    * `__height` -> `height`
    * `__x` -> `x`
    * `__y` -> `y`
* Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
    * Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
    * Assign each argument `width`, `height`, `x` and `y` to the right attribute

Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to vet/validate what a developer is trying to assign to a variable.

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 3. Validate attributes
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):
* If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`
* If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`
* If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 4. Area first
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 5. Display #0
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 6. __str__
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 7. Display #1
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 8. Update #0
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:
* 1st argument should be the `id` attribute
* 2nd argument should be the `width` attribute
* 3rd argument should be the `height` attribute
* 4th argument should be the `x` attribute
* 5th argument should be the `y` attribute

As there are no keywords to identify each argument, order is important.

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 9. Update #1
Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:
* `**kwargs` can be thought of as a double pointer to a dictionary: key/value
    * As Python doesn’t have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
* `**kwargs` must be skipped if `*args` exists and is not empty
* Each key in this dictionary represents an attribute to the instance

Since each argument has an associated keyword, order is not important.

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 10. And now, the Square!
Write the class `Square` that inherits from `Rectangle`:
* Class constructor: `def __init__(self, size, x=0, y=0, id=None):`
    * Call the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the `Rectangle` class. The `width` and `height` must be assigned to the value of `size`
    * You must not create new attributes for this class, use all attributes of `Rectangle` (after all, a square is simply a rectangle with the same width and height)
    * All `width`, `height`, `x` and `y` validation must inherit from `Rectangle` - same behavior in case of wrong data
* The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height`

As you know, a square is a special rectangle, so it makes sense this class `Square` inherits from `Rectangle`. Now you have a `Square` class which has the same attributes and same methods.

File(s): [`models/rectangle.py`](./models/rectangle.py)

### :white_check_mark: 11. Square size
Update the class `Square` by adding the public getter and setter `size`
* The setter should assign (in this order) the `width` and the `height` - with the same value
* The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`)

File(s): [`models/square.py`](./models/square.py)

### :white_check_mark: 12. Square update
Update the class `Square` by adding the public method `def update(self, *args, **kwargs):` that assigns attributes:
* `*args` is the list of arguments - no-keyworded arguments
    * 1st argument should be the `id` attribute
    * 2nd argument should be the `size` attribute
    * 3rd argument should be the `x` attribute
    * 4th argument should be the `y` attribute
* `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
* `**kwargs` must be skipped if *args exists and is not empty
* Each key in this dictionary represents an attribute to the instance

File(s): [`models/square.py`](./models/square.py)

### :white_check_mark: 13. Rectangle instance to dictionary representation
Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`:

This dictionary must contain:
* `id`
* `width`
* `height`
* `x`
* `y`

File(s): [`models/square.py`](./models/square.py)

### :white_check_mark: 14. Square instance to dictionary representation
Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`:

This dictionary must contain:
* `id`
* `size`
* `x`
* `y`

File(s): [`models/square.py`](./models/square.py)

### :white_check_mark: 15. Dictionary to JSON string
JSON is one of the standard formats for sharing data representation.

Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`:
* `list_dictionaries` is a list of dictionaries
* If `list_dictionaries` is `None` or empty, return the string: `"[]"`
* Otherwise, return the JSON string representation of `list_dictionaries`

File(s): [`models/base.py`](./models/base.py)

### :white_check_mark: 16. JSON string to file
Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file:
* `list_objs` is a list of instances which inherit from `Base` - example: list of `Rectangle` or list of `Square` instances
* If `list_objs` is `None`, save an empty list
* The filename must be: `<Class name>.json` - example: `Rectangle.json`
* You must use the static method `to_json_string` (created before)
* You must overwrite the file if it already exists

File(s): [`models/base.py`](./models/base.py)

### :white_check_mark: 17. JSON string to dictionary
Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`:
* `json_string` is a string representing a list of dictionaries
* If `json_string` is `None` or empty, return an empty list
* Otherwise, return the list represented by `json_string`

File(s): [`models/base.py`](./models/base.py)

### :white_check_mark: 18. Dictionary to Instance
Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set:
* `**dictionary` can be thought of as a double pointer to a dictionary
* To use the `update` method to assign all attributes, you must create a “dummy” instance before:
    * Create a `Rectangle` or `Square` instance with “dummy” mandatory attributes (width, height, size, etc.)
    * Call `update` instance method to this “dummy” instance to apply your real values
* You must use the method `def update(self, *args, **kwargs):`
* `**dictionary` must be used as `**kwargs` of the method `update`
* You are not allowed to use `eval`

File(s): [`models/base.py`](./models/base.py)

### :white_check_mark: 19. File to instances
Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances:
* The filename must be: `<Class name>.json` - example: `Rectangle.json`
* If the file doesn’t exist, return an empty list
* Otherwise, return a list of instances - the type of these instances depends on `cls` (current class using this method)
* You must use the `from_json_string` and `create` methods (implemented previously)

File(s): [`models/base.py`](./models/base.py)

## Advanced Tasks

### :white_check_mark: 20. JSON ok, but CSV?
Update the class `Base` by adding the class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in CSV:
* The filename must be: `<Class name>.csv` - example: `Rectangle.csv`
* Has the same behavior as the JSON serialization/deserialization
* Format of the CSV:
    * Rectangle: `<id>,<width>,<height>,<x>,<y>`
    * Square: `<id>,<size>,<x>,<y>`

File(s): [`models/base.py`](./models/base.py)

### :white_large_square: 21. Let's draw it
Update the class `Base` by adding the static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangle`s and `Square`s:
* You must use the [Turtle graphics module](https://docs.python.org/3.0/library/turtle.html)
* To install it: `sudo apt-get install python3-tk`
* To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: `config.ssh.forward_x11 = true`
* No constraints for color, shape etc… be creative!

To set up X11 forwarding for your Vagrant vm:
* Change line `# ForwardX11 no` in `/etc/ssh/ssh_config` to `ForwardX11 yes`
* Add lines `config.ssh.forward_agent = true` and `config.ssh.forward_x11 = true` to your Vagrantfile
* Restart your vm with `vagrant reload`, then `vagrant ssh`
* If you get an error that looks like `/usr/bin/xauth: timeout in locking authority file /home/vagrant/.Xauthority`, then enter `rm .Xauthority` (perhaps with `sudo`)
* Restart the vm again
* Test with xeyes - if Xquartz is installed on the Mac OS it should open in an Xquartz window.

File(s): [`models/base.py`](./models/base.py)

---

## Student
* **Samuel Pomeroy** - [allelomorph](github.com/allelomorph)
