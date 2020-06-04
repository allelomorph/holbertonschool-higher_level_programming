#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 12. Student to JSON with filter"""


class Student:
    """Simple class containing student data.

    Args:
        first_name (str): given name of student
        last_name (str): family name of student
        age (int): age of student in years

    Attributes:
        first_name (str): given name of student
        last_name (str): family name of student
        age (int): age of student in years

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of self, minus any elements
        whose keys are are not listed in `attrs`. If `attrs` is not a list of
        strings, returns entire dict of self.

        Args:
            attrs (list) of (str): list of keys for items in dictionary

        Returns:
            `ret_dict`, a dictionary for all of the keys listed in `attrs`,
        or self__dict__ if there are any type conflicts for `attrs`.

        """

        ret_dict = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return self.__dict__
            for key in attrs:
                if key in self.__dict__:
                    ret_dict.update({key: self.__dict__[key]})
            return ret_dict
        else:
            return self.__dict__
