#!/usr/bin/python3
"""Square generation module for Python project 0x06
"""


class Square:
    """Class defined for square generation.

    Args:
        size (int): length of one side of square

    Attributes:
        __size (int): length of one side of square

    """

    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        """Calulates area of square.

        Attributes:
            __size (int): length of one side of square

        Returns:
            area (int): length of one side, squared

        """
        area = self.__size * self.__size
        return area

    def __lt__(self, other):
        """Define comparisons of class object for less than.
        Taken from PEP 207 -- Rich Comparisons
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Define comparisons of class object for less than/equal to.
        Taken from PEP 207 -- Rich Comparisons
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Define comparisons of class object for equal to.
        Taken from PEP 207 -- Rich Comparisons
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Define comparisons of class object for not equal to.
        Taken from PEP 207 -- Rich Comparisons
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Define comparisons of class object for greater than.
        Taken from PEP 207 -- Rich Comparisons
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Define comparisons of class object for greater than/equal to.
        Taken from PEP 207 -- Rich Comparisons
        """
        return self.area() >= other.area()
