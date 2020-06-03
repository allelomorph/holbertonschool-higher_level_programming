#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 8 """


class BaseGeometry:
    """Intentionally empty area() method.

    """
    def area(self):
        """Unimplemented, only raises exception to notify user.

        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Input filtration for integers: checks if value is an int above 0.
        No use of self, could be staticmethod.

        Args:
            name (str): name bound to object
            value (any): value of object, expecting int

        Exceptions:
            TypeError: if `value` is not an int
            ValueError: if `value` is less than or equal to 0

        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry, for use with rectangular constructs.

    Args:
        width (int): x dimension of rectangle
        height (int): y dimension of rectangle

    Attributes:
        __width (int): x dimension of rectangle
        __height (int): y dimension of rectangle

    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns rectangle area as width * height.

        Attributes:
            __width (int): x dimension of rectangle
            __height (int): y dimension of rectangle

        Returns:
            __width * __height

        """
        return self.__width * self.__height

    def __str__(self):
        """ Provides printable representation of Rectangle object.

        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)


class Square(Rectangle):
    """Inherits from Rectangle and thus from BaseGeometry, for use with
    rectangular constructs of equal sides.

    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns square area as size * size, invoking Rectangle.area().

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """
        return self.__size ** 2

    def __str__(self):
        """ Provides printable representation of Square object.

        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
