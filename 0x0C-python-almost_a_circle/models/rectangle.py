#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 2 - 13"""
from models.base import Base


class Rectangle(Base):
    """Creates rectangle objects with 2 dimensions and offset coordinates.

    Uses superclass `__init__` to create valid instance id, and sets
    self vars from args.

    Args:
        width (int): x dimension of rectangle
        height (int): y dimension of rectangle
        x (int): horizontal offset of rectangle
        y (int): vertical offset of rectangle
        id (int): unique identifer for each instance of super()

    Project task:
        2. First Rectangle - __init__, getters and setters for `width`,
            `height`, `x`, `y`

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __integer_validator(self, attr, value):
        """Validates incoming argument values for use with internal attributes.

        Args:
            attr (str): name of intended attribute assignment
            value (any): expecting int, but will filter out other types

        Raises:
            TypeError: if any incoming value is not (int)
            ValueError: if any `width` or `height` candidate is <= 0, or if
                `x` or `y` candidates are < 0

        Project task:
            3. Validate attributes - input validation for `width`, `height`,
                `x`, `y`

        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attr))
        if attr is 'width' or attr is 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attr))
        elif attr is 'x' or attr is 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attr))

    @property
    def width(self):
        """`__width` getter

        Returns:
            __width (int): x dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): x dimension of rectangle

        Attributes:
            __width (int): x dimension of rectangle

        """
        self.__integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """`__height` getter

        Returns:
            __height (int): y dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): y dimension of rectangle

        Attributes:
            __height (int): y dimension of rectangle

        """
        self.__integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """`__x` getter

        Returns:
            __x (int): horizontal offset of rectangle

        """
        return self.__x

    @x.setter
    def x(self, value):
        """Args:
            value (int): horizontal offset of rectangle

        Attributes:
            __x (int): horizontal offset of rectangle
        """
        self.__integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """`__y` getter

        Returns:
            __y (int): vertical offset of rectangle

        """
        return self.__y

    @y.setter
    def y(self, value):
        """Args:
            value (int): vertical offset of rectangle

        Attributes:
            __y (int): vertical offset of rectangle

        """
        self.__integer_validator('y', value)
        self.__y = value

    def area(self):
        """Returns area of rectangle as product of `width` and `height`.

        Returns:
            `__width` * `__height`

        Project tasks:
            4. Area first - public method `area()`

        """
        return self.width * self.height

    def display(self):
        """Prints representation of rectangle to stdout using '#'.

        Attributes:
            display (str): printed as ASCII art drawing of rectangle
            __display (str): final value of `display` saved to instance
                attribute for unit testing

        Project tasks:
            5. Display #0 - public method `display()`, only use `width`
        and `height`
            7. Display #1 - include use of offset vars `x` and `y`

        """
        display = ''
        for row in range(self.y):
            display += '\n'
        for row in range(self.height):
            for column in range(self.x):
                display += ' '
            for column in range(self.width):
                display += '#'
            if row < self.height - 1:
                display += '\n'
        self.__display = display
        print(display)

    def __str__(self):
        """Returns string with numeric representation of rectangle

        Returns:
            '[Rectangle] (<id>) <x>/<y> - <width>/<height>'

        Project tasks:
            6. __str__ - `__str__` method

        """
        return ('[Rectangle] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}/{:d}'.format(self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Updates attributes in a given order based on variable amount of
        non-keyword args, or in any order with keyword args.

        `*args` takes precedence over `**kwargs`: if any non-keyword args are
        present, keyword args are ignored.

        Args (non-keyword, in order of appearance in variable list):
            id (int): identifer for instances of `super()`
            width (int): x dimension of rectangle
            height (int): y dimension of rectangle
            x (int): horizontal offset of rectangle
            y (int): vertical offset of rectangle

        Keyword args:
            any of the above if key matches arg name

        Raises:
            TypeError: if amount of arguments given not between 1 and 5 (not
                in project instructions)
            KeyError: if keyword not among class and superclass getters

        Project tasks:
            8. Update #0 - updates `id`, `width`, `height`, `x`, or `y` based
                on amount of args using *args
            9. Update #1 - adds use of **kwargs to access key-worded argments
                in any order. if *args not empty, **kwargs skipped

        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 5:
                raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                                ' or 1 to 5 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                        Base._Base__assigned_ids.add(value)
                    elif key == 'width':
                        self.width = value
                    elif key == 'height':
                        self.height = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 5:
            raise TypeError('Rectangle.update() takes 1 to 5 keyword,' +
                            ' or 1 to 5 non-keyword arguments')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        self.id = arg
                        Base._Base__assigned_ids.add(arg)
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

    def to_dictionary(self):
        """Creates dictionary representation of self without revealing private
        attribute names, as would __dict__.

        Returns:
            self_dict (dict): custom dictionary of private attribute values
                populated using getters

        Project tasks:
            13. Rectangle instance to dictionary representation

        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['width'] = self.width
        self_dict['height'] = self.height
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
