The ``0-add_integer`` module
============================
This module contains only one function: add_integer.

Using ``add_integer``
---------------------

First import
~~~~~~~~~~~~
First import ``add_integer`` from the ``0-add_integer`` module. Since the file name contains a numeral, you can't use the simple ``from 0-add_integer import add_integer``. You can instead use the following syntax:

    >>> add_integer = __import__('0-add_integer').add_integer

Normal use
~~~~~~~~~~
Now add_integer can be used to calculate the sum of two integers:

    >>> add_integer(1, 2)
    3

    >>> add_integer(100, -4)
    96

Note that the function can take floating point values as well as integers, but they will be cast to int and thus rounded down:

    >>> add_integer(3.456, 4)
    7

    >>> add_integer(23.167, 27.8567)
    50

    >>> add_integer(3.456, -4)
    -1

Also, the second argument defaults to 98, so entering only one argument is possible if you just want to add it to 98:

    >>> add_integer(5)
    103

    >>> add_integer(3.456)
    101

Exceptions
~~~~~~~~~~
If a and b are any type other than int or float, the function will raise a TypeError exception with the message ``a must be an integer`` or ``b must be an integer.``

    >>> add_integer('5')
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(3, [5])
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    >>> add_integer((3, 5))
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

Of course, there are some limits to the floats that can be handled:

    >>> pos_inf = float('inf')  # positive infinity
    >>> add_integer(pos_inf, 4.0)
    Traceback (most recent call last):
        ...
    OverflowError: cannot convert float infinity to integer

    >>> neg_inf = float('-inf')  # negative infinity
    >>> add_integer(neg_inf, 4.0)
    Traceback (most recent call last):
        ...
    OverflowError: cannot convert float infinity to integer

    >>> not_a_num = float('nan')   # NaN ("not a number", )
    >>> add_integer(not_a_num, 4.0)
    Traceback (most recent call last):
        ...
    ValueError: cannot convert float NaN to integer

Additionally, there should be one or two arguments provided, otherwise an exception will occur:

    >>> add_integer()
    Traceback (most recent call last):
        ...
    TypeError: add_integer() missing 1 required positional argument: 'a'

    >>> add_integer(1, 2, 3)
    Traceback (most recent call last):
        ...
    TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given
