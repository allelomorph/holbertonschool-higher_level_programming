#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 8 """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle and thus from BaseGeometry, for use with
    rectangular constructs of equal sides.

    Args:
        size (int): length of side of square

    Attributes:
        __size (int): length of side of square

    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns square area as size * size.

        * Required by task instructions, but overloading Rectangle.area() is
        redundant here, as it has the same result.

        Attributes:
            __size (int): length of side of square

        Returns:
            __size ** 2

        """
        return self.__size ** 2
'''
