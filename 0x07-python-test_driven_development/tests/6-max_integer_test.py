#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_type(self):
        """The argument 'list' must be an iterable type such as list, tuple or
        str; or a TypeError will arise. Sets are iterable but not indexable,
        which will also cause a TypeError.
        """
        # TypeError raised when list is not an iterable type
        self.assertRaises(TypeError, max_integer, 5)
        self.assertRaises(TypeError, max_integer, True)
        # TypeError also for sets, as they cannot be indexed
        self.assertRaises(TypeError, max_integer, {3, 5})
        # program intended for lists
        self.assertEqual(max_integer([3, 5]), 5)
        # but also works with tuples
        self.assertEqual(max_integer((3, 5)), 5)
        # and strings, with each character evaluted by ASCII value
        self.assertEqual(max_integer('actg'), 't')
        # empty iterables produce no output
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer(''), None)

    def test_first_list_dimension_type(self):
        """ASCII chars are implicity converted to int by '>' comparison.
        Strings need to be with their own type, but ints, floats, and bools
        can all be evaluated together: True as 1, and False as 0. If largest
        value is a float, it is returned as a float.
        """
        # strings compare ASCII values
        self.assertEqual(max_integer(['a', 'b']), 'b')
        # but no mixing with other types
        self.assertRaises(TypeError, max_integer, [3, 'a'])
        # ints and floats evaluate togther
        self.assertEqual(max_integer([3, 5.0]), 5.0)
        self.assertEqual(max_integer([3, -5.3456]), 3)
        # as well as with bools
        self.assertEqual(max_integer([-1, -.5, False]), False)
        self.assertEqual(max_integer([5, .544, True]), 5)

    def test_higher_list_dimensions(self):
        """First dimension list members can themselves also be iterables (except
        sets, as they always return <list>[0].) Those iterables can be of
        varying length in the same dimension, but must all be of the same
        dimensional depth to avoid a TypeError in comparison. For comparison of
        any values in elements with dimensions beyond the first, it will always
        be the first value to be compared by the program: <list>[i][0][0]...,
        <list>[i + 1][0][0]..., ...
        """
        # 2nd dimension lists of variable length but same depth
        self.assertEqual(max_integer([[5, 4, 1], [6, 3], []]), [6, 3])
        # same for tuples and strings
        self.assertEqual(max_integer([(5, 4, 1), (6, 3), ()]), (6, 3))
        self.assertEqual(max_integer(['azzz', 'byy', 'cx']), 'cx')
        # higher dimensions are possible, but all must be same depth, and only
        # first members are compared
        self.assertEqual(max_integer([[[1, 2], [2], []], [[4], [5]], [[6]]]),
                         [[6]])
        self.assertEqual(max_integer([[[8, 2], [2], []], [[4], [5]], [[6]]]),
                         [[8, 2], [2], []])
        # list or tuple member sets always return index 0, so are not useful
        self.assertEqual(max_integer([{5, 4}, {6, 3, 1}, {20}]), {4, 5})

    def test_list_length(self):
        """The argument 'list' can be an iterable datatype (aside from sets)
        of any length, including 1 or 0 members, except for tuples, which need
        at least 2 members to be evaluated as that type.
        """
        # empty iterables produce no output
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(()), None)
        self.assertEqual(max_integer(''), None)
        # length of 1 element simply returns that element for lists and strings
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer('a'), 'a')
        # but a single member tuple is just evaulated as that member
        self.assertRaises(TypeError, max_integer, (5))

if __name__ == '__main__':
    unittest.main()
