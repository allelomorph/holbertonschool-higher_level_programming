#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 10 - 14"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Creates square objects with 2 dimensions and offset coordinates.

    Uses super-superclass `Base` __init__ to create valid instance id,
    and passes args to superclass `__init__` to set attributes. Does not
    create its own attributes. `size` acts as alias for `width`/`height`.

    Args:
        size (int): x and y dimensions of square
        x (int): horizontal offset of square
        y (int): vertical offset of square
        id (int): unique identifer for each instance of super().super()

    Project task:
        10. And now, the Square! - class Square `__init__`, `__str__`,
            only inherited validation, no new attributes

    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string with numeric representation of square

        Returns:
            '[Square] (<id>) <x>/<y> - <size>'

        Project task:
            10. And now, the Square! - class Square `__init__`, `__str__`,
                only inherited validation, no new attributes
        """
        return ('[Square] ({:d}) {:d}/'.format(self.id, self.x) +
                '{:d} - {:d}'.format(self.y, self.width))

    @property
    def size(self):
        """`size` getter, but in this case `size` acts as alias for
        `width`/`height`.

        Returns:
            __size (int): x and y dimensions of square

        Project task:
            11. Square size - public getter and setter `size`, using
                validation from super().width

        """
        return self.width

    @size.setter
    def size(self, value):
        """`size` setter, but in this case `size` acts as alias for
        `width`/`height`.

        Args:
            value (int): x and y dimensions of square

        Project task:
            11. Square size - public getter and setter `size`, using
                validation from super().width

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates superclass attributes in a given order based on variable
        amount of non-keyword args, or in any order with keyword args.

        `*args` takes precedence over `**kwargs`: if any non-keyword args are
        present, keyword args are ignored.

        Args (non-keyword, in order of appearance in variable list):
            id (int): unique identifer for each instance of super()
            size (int): x and y dimensions of square
            x (int): horizontal offset of rectangle
            y (int): vertical offset of rectangle

        Keyword args:
            any of the above if key matches arg name

        Raises:
            TypeError: if amount of consecutive non-keyword or keyword
                arguments given not between 1 and 4 (not in task instructions)
            KeyError: if keyword not among superclass and super-superclass
                getters

        Project tasks:
            12. Square update - updates `id`, `size`, `x`, or `y` based on
                *args, or uses **kwargs to access key-worded argments in
                any order. if *args not empty, **kwargs skipped

        """
        if len(args) == 0:
            if len(kwargs) == 0 or len(kwargs) > 4:
                raise TypeError('Square.update() takes 1 to 4 keyword,' +
                                ' or 1 to 4 non-keyword arguments')
            else:
                for key, value in kwargs.items():
                    if key == 'id':
                        if self.id != value:
                            temp = self.id
                            self.id = value
                            Base._Base__assigned_ids.remove(temp)
                            Base._Base__assigned_ids.add(value)
                    elif key == 'size':
                        self.size = value
                    elif key == 'x':
                        self.x = value
                    elif key == 'y':
                        self.y = value
                    else:
                        raise KeyError('invalid attribute name: ' +
                                       '{}'.format(key))
        elif len(args) > 4:
            raise TypeError('Square.update() takes 1 to 4 keyword,' +
                            ' or 1 to 4 non-keyword arguments')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    if self.id != arg:
                        temp = self.id
                        self.id = arg
                        Base._Base__assigned_ids.remove(temp)
                        Base._Base__assigned_ids.add(arg)
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

    def to_dictionary(self):
        """Creates dictionary representation of self without revealing private
        attribute names, as would __dict__.

        Returns:
            self_dict (dict): custom dictionary of private attribute values
                populated using getters

        Project tasks:
            14. Square instance to dictionary representation

        """
        self_dict = dict()
        self_dict['id'] = self.id
        self_dict['size'] = self.size
        self_dict['x'] = self.x
        self_dict['y'] = self.y
        return self_dict
