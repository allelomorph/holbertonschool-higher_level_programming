#!/usr/bin/python3
"""Unittest for base({..]) after task 1"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests `Base` class."""

    @classmethod
    def setUpClass(cls):
        """Alerts user to any instances of tested classes or subclasses not
        already cleaned up.

        """
        b_obj = Base._Base__nb_objects
        b_ids = Base._Base__assigned_ids
        if b_obj > 1:
            print('testBase: previous Base counter not reset,' +
                  'now at: {}'.format(b_obj))
        if len(b_ids) > 0:
            print('testBase: previous Base ids still potentially in' +
                  'use: {}'.format(b_ids))

    def tearDown(self):
        """Reinitializes obejct iterator and set of assigned ids.

        """
        b_ids = Base._Base__assigned_ids
        Base._Base__nb_objects = 0
        b_obj = Base._Base__nb_objects
        b_ids.clear()
        if b_obj > 1:
            print('testBase: Base counter not reset, now at: {}'.format(b_obj))
        if len(b_ids) > 0:
            print('testBase: previous Base ids still potentially in' +
                  'use: {}'.format(b_ids))

    def test_id(self):
        """Task 1. Base class
        According to project specs, `id` can be assumed to be an integer,
        so TypeError testing omitted.

        """
        # ValueError: assigning id of 0
        self.assertRaises(ValueError, Base, 0)
        # ValueError: assigning negative ids
        self.assertRaises(ValueError, Base, -5)
        # Normal use: Assigning postive id
        b1 = Base(3)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b1.serial, 1)
        # No argument defaults to assigning current count of instances
        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.serial, 2)
        # Further instance w/o arg continues pattern, even if id already used
        b3 = Base()
        self.assertEqual(b3.id, 3)
        self.assertEqual(b3.serial, 3)
        # Manually assigning id that has already automatically been assigned
        b4 = Base(3)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b1.serial, 1)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b3.serial, 3)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b4.serial, 4)

    def test_to_json_string(self):
        """15. Dictionary to JSON string"""
        # Normal use: 1 arg (list) of (dict)
        d_list = [{'id': 10}, {'id': 15}]
        self.assertEqual(Base.to_json_string(d_list),
                         '[{"id": 10}, {"id": 15}]')
        # Empty list
        self.assertEqual(Base.to_json_string([]), '[]')
        # None list
        self.assertEqual(Base.to_json_string(None), '[]')
        # deprecated use: list not of dicts
        lst = [2, 3, 4]
        self.assertEqual(Base.to_json_string(lst), '[2, 3, 4]')
        # TypeError: no args
        self.assertRaises(TypeError, Base.to_json_string)
        d_list2 = [{'id': 20}]
        # TypeError: 2+ args
        self.assertRaises(TypeError, Base.to_json_string, d_list, d_list2)

    def test_save_to_file(self):
        """16. JSON string to file

        AttributeError: .to_dictionary() not in `Base`, only Square/Rectangle.

        Testing of `save_to_file` done in `TestRectangle` and `TestSquare`.

        """
        # Empty list
        # None list
        # arg not an iterable type
        # arg not a list, but tuple or set
        # arg list contents not Squares or Rectangles (no to_dictionary())
        # class of list objects does not match class that called save_to_file
        # no args
        # 2+ args
        pass

    def test_from_json_string(self):
        """17. JSON string to dictionary"""
        # Normal use: 1 arg (str)
        a = Base.from_json_string('[{"id": 10}, {"id": 15}]')
        self.assertEqual(a, [{'id': 10}, {'id': 15}])
        # Empty str
        b = Base.from_json_string('')
        self.assertEqual(b, [])
        # None str
        c = Base.from_json_string(None)
        self.assertEqual(c, [])
        # TypeError: no args
        self.assertRaises(TypeError, Base.from_json_string)
        # TypeError: 2+ args
        self.assertRaises(TypeError, Base.from_json_string, a, b)

    def test_create(self):
        """18. Dictionary to Instance

        TypeError: __init__ for `Base` takes 1 arg, and `create` uses 2 to
        make `temp`.

        Testing of `create` done in `TestRectangle` and `TestSquare`.

        """
        # no args
        # with any non-keyword args
        # dict has bad key
        # dict has too many keys
        # dict has no keys
        pass

    def test_load_from_file(self):
        """19. File to instances

        `load_from_file` uses `create`, and so must be tested in subclasses

        Testing of `create` done in `TestRectangle` and `TestSquare`.

        """
        # Normal use: file with JSON string of instances as dicts
        # empty file
        # empty list in file
        # file has other content / not in JSON
        # file inaccessible
        # mixed square and rectangle objects represented in string
        # any dict has bad key
        # any dict has too many keys
        # any dict has no keys
        pass

if __name__ == '__main__':
    unittest.main()
