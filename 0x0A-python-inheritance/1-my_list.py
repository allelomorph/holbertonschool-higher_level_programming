#!/usr/bin/python3
""" 0x0A. Python - Inheritance, task 1 """


class MyList(list):
    """Custom list type intended to only contain integers.

    """

    def print_sorted(self):
        """Prints MyList lists in ascending order by value.

        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
