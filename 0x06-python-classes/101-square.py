#!/usr/bin/python3
"""Square generation module for Python project 0x06
"""


class Square:
    """Class defined for square generation.

    Args:
        size (int): length of one side of square
        position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines


    Attributes:
        __size (int): length of one side of square
        __position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines

    """

    def __init__(self, size=0, position=(0, 0)):
        # attribute assigment here engages setters defined below
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size getter, setter with same method name

        Returns:
            __size (int): length of one side, squared

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side of square

        Attributes:
            __size (int): length of one side of square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """__position getter, setter with same method name

        Returns:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Args:
            value (tuple): tuple of two positive integers

        Attributes:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        Raises:
            TypeError: if value is not a tuple of two positive ints

        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

    def area(self):
        """Calulates area of square.

        Attributes:
            __size (int): length of one side of square

        Returns:
            area (int): length of one side, squared

        """
        area = self.__size * self.__size
        return area

    def str_format(self):
        """formats text representation of square in hash chars,
        horizontally and vertically offset by first and second int
        in __position, respectively.

        Attributes:
            __size (int): length of one side of square
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        """
        str = ''
        if self.__size is 0:
            str += '\n'
        else:
            for v_offset in range(0, self.__position[1]):
                str += '\n'
            for row in range(0, self.__size):
                for h_offset in range(0, self.__position[0]):
                    str += ' '
                for col in range(0, self.__size):
                    str += '#'
                str += '\n'
        return str

    def my_print(self):
        """Prints text representation of square in hash chars,
        horizontally and vertically offset by first and second int
        in __position, respectively.

        """
        print(self.str_format(), end="")

    def __str__(self):
        """Returns: self.str_format() minus trailing newline

        """
        length = len(self.str_format())
        truncated = self.str_format()[:length - 1]
        return truncated
