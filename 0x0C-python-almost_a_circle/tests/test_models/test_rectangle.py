#!/usr/bin/python3
"""Unittest for Rectangle([..]) to task 13, and inheritance for 15-19

# with `unittest discover` the functions are run in alpha order by name of
class, then func name.

"""
import unittest
import contextlib  # for redirecting stdout during print tests
import os  # for tearDownClass and test_load_from_file
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests `Rectangle` class, subclass of `Base`.

    """
    @classmethod
    def setUpClass(cls):
        """Alerts user to any instances of tested classes or subclasses not
        already cleaned up.

        """
        b_obj = Base._Base__nb_objects
        b_tobj = Base._Base__true_nb_objects
        b_ids = Base._Base__assigned_ids
        if b_obj > 1:
            print('testRectangle: previous Base counter not reset, ' +
                  'now at: {}'.format(b_obj))
        if b_tobj > 1:
            print('testRectangle: previous total Base counter not reset, ' +
                  'now at: {}'.format(b_tobj))
        if len(b_ids) > 0:
            print('testRectangle: previous Base ids still potentially in ' +
                  'use: {}'.format(b_ids))

    def tearDown(self):
        """Deletes test files. Reinitializes `Base` object iterator and set
        of assigned ids.

        """
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        Rectangle._Base__nb_objects = 0
        Rectangle._Base__true_nb_objects = 0
        Rectangle._Base__assigned_ids.clear()
        r_obj = Rectangle._Base__nb_objects
        r_tobj = Rectangle._Base__true_nb_objects
        r_ids = Rectangle._Base__assigned_ids
        if r_obj > 1:
            print('testRectangle: Rectangle counter not reset, ' +
                  'now at: {}'.format(r_obj))
        if r_tobj > 1:
            print('testRectangle: total Rectangle counter not reset, ' +
                  'now at: {}'.format(r_tobj))
        if len(r_ids) > 0:
            print('testRectangle: Rectangle ids potentially still in ' +
                  'use: {}'.format(r_ids))
        Base._Base__nb_objects = 0
        Base._Base__true_nb_objects = 0
        Base._Base__assigned_ids.clear()
        b_obj = Base._Base__nb_objects
        b_tobj = Base._Base__true_nb_objects
        b_ids = Base._Base__assigned_ids
        if b_obj > 1:
            print('testBase: Base counter not reset, now at: {}'.format(b_obj))
        if b_tobj > 1:
            print('testBase: total Base counter not reset, ' +
                  'now at: {}'.format(b_obj))
        if len(b_ids) > 0:
            print('testBase: Base ids potentially still in ' +
                  'use: {}'.format(b_ids))

    def test_arg_count(self):
        """Task 2. First Rectangle"""
        # TypeError: 0 args
        self.assertRaises(TypeError, Rectangle)
        # TypeError: 1 arg
        self.assertRaises(TypeError, Rectangle, 3)
        # Normal use: 2 args - x, y default to 0, id defaults to serial
        r1 = Rectangle(3, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        # Normal use: 3 args - y defaults to 0, id defaults to serial
        r2 = Rectangle(3, 3, 3)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r2.id, 2)
        # Normal use: 4 args - id defaults to serial
        r3 = Rectangle(3, 3, 3, 3)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 3)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.serial, 3)
        # Normal use: 5 args - no defaults
        r4 = Rectangle(3, 3, 3, 3, 20)
        self.assertEqual(r4.x, 3)
        self.assertEqual(r4.y, 3)
        self.assertEqual(r4.id, 20)
        self.assertEqual(r4.serial, 4)
        # TypeError: over 5 args
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, 3, 3, 3)

    def test_width_value(self):
        """Task 3. Validate attributes"""
        # Normal use: width is int > 0
        r5 = Rectangle(3, 3)
        self.assertEqual(r5.id, 1)
        self.assertEqual(r5.width, 3)
        # ValueError: width is int 0
        self.assertRaises(ValueError, Rectangle, 0, 3)
        # ValueError width is int < 0
        self.assertRaises(ValueError, Rectangle, -3, 3)
        # TypeError: width is float
        self.assertRaises(TypeError, Rectangle, 3.0, 3)
        # TypeError: width is str
        self.assertRaises(TypeError, Rectangle, '3', 3)
        # TypeError: width is tuple
        self.assertRaises(TypeError, Rectangle, (3,), 3)
        # TypeError: width is list
        self.assertRaises(TypeError, Rectangle, [3], 3)
        # TypeError: width is bool
        self.assertRaises(TypeError, Rectangle, True, 3)
        # TypeError: width is set
        self.assertRaises(TypeError, Rectangle, {3, 4}, 3)
        # TypeError: width is None
        self.assertRaises(TypeError, Rectangle, None, 3)

    def test_height_value(self):
        """Task 3. Validate attributes"""
        # Normal use: height is int > 0
        r6 = Rectangle(3, 3)
        self.assertEqual(r6.id, 1)
        self.assertEqual(r6.height, 3)
        # ValueError: height is int 0
        self.assertRaises(ValueError, Rectangle, 3, 0)
        # ValueError height is int < 0
        self.assertRaises(ValueError, Rectangle, 3, -3)
        # TypeError: height is float
        self.assertRaises(TypeError, Rectangle, 3, 3.0)
        # TypeError: height is str
        self.assertRaises(TypeError, Rectangle, 3, '3')
        # TypeError: height is tuple
        self.assertRaises(TypeError, Rectangle, 3, (3,))
        # TypeError: height is list
        self.assertRaises(TypeError, Rectangle, 3, [3])
        # TypeError: height is bool
        self.assertRaises(TypeError, Rectangle, 3, True)
        # TypeError: height is set
        self.assertRaises(TypeError, Rectangle, 3, {3, 4})
        # TypeError: height is None
        self.assertRaises(TypeError, Rectangle, 3, None)

    def test_x_value(self):
        """Task 3. Validate attributes"""
        # Normal use: x is int > 0
        r7 = Rectangle(3, 3, 3)
        self.assertEqual(r7.id, 1)
        self.assertEqual(r7.x, 3)
        # Normal use: x is int 0
        r8 = Rectangle(3, 3, 0)
        self.assertEqual(r8.id, 2)
        self.assertEqual(r8.x, 0)
        # ValueError: x is int < 0
        self.assertRaises(ValueError, Rectangle, 3, 3, -3)
        # TypeError: x is float
        self.assertRaises(TypeError, Rectangle, 3, 3, 3.0)
        # TypeError: x is str
        self.assertRaises(TypeError, Rectangle, 3, 3, '3')
        # TypeError: x is tuple
        self.assertRaises(TypeError, Rectangle, 3, 3, (3,))
        # TypeError: x is list
        self.assertRaises(TypeError, Rectangle, 3, 3, [3])
        # TypeError: x is bool
        self.assertRaises(TypeError, Rectangle, 3, 3, True)
        # TypeError: x is set
        self.assertRaises(TypeError, Rectangle, 3, 3, {3, 4})
        # TypeError: x is None
        self.assertRaises(TypeError, Rectangle, 3, 3, None)

    def test_y_value(self):
        """Task 3. Validate attributes"""
        # Normal use: y is int > 0
        r9 = Rectangle(3, 3, 3, 3)
        self.assertEqual(r9.id, 1)
        self.assertEqual(r9.y, 3)
        # Normal use: y is int 0
        r10 = Rectangle(3, 3, 3, 0)
        self.assertEqual(r10.id, 2)
        self.assertEqual(r10.y, 0)
        # ValueError: y is int < 0
        self.assertRaises(ValueError, Rectangle, 3, 3, 3, -3)
        # TypeError: y is float
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, 3.0)
        # TypeError: y is str
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, '3')
        # TypeError: y is tuple
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, (3,))
        # TypeError: y is list
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, [3])
        # TypeError: y is bool
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, True)
        # TypeError: y is set
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, {3, 4})
        # TypeError: y is None
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, None)

    def test_area(self):
        """Task 4. Area first"""
        # Normal use: no args
        r11 = Rectangle(2, 10)
        self.assertEqual(r11.id, 1)
        self.assertEqual(r11.area(), 20)
        # Error: use any args
        self.assertRaises(TypeError, r11.area, 5)

    def test_display_0(self):
        """Task 5. Display #0"""
        # Normal use: no args to display, no x/y given
        r12 = Rectangle(2, 2)
        self.assertEqual(r12.id, 1)
        with contextlib.redirect_stdout(None):
            r12.display()
        self.assertEqual(r12._Rectangle__display, '##\n##')
        # Error: use any args to display
        self.assertRaises(TypeError, r12.display, 5)

    def test_display_1(self):
        """Task 7. Display #1"""
        # Normal use: no args to display, x given
        r13 = Rectangle(2, 2, 2)
        self.assertEqual(r13.id, 1)
        with contextlib.redirect_stdout(None):
            r13.display()
        self.assertEqual(r13._Rectangle__display, '  ##\n  ##')
        # Normal use: no args to display, only y given (via update)
        r14 = Rectangle(2, 2)
        self.assertEqual(r14.id, 2)
        self.assertEqual(r14.y, 0)
        r14.update(y=2)
        self.assertEqual(r14.y, 2)
        with contextlib.redirect_stdout(None):
            r14.display()
        self.assertEqual(r14._Rectangle__display, '\n\n##\n##')
        # Normal use: no args to display, x/y given
        r15 = Rectangle(2, 2, 2, 2)
        self.assertEqual(r15.id, 3)
        with contextlib.redirect_stdout(None):
            r15.display()
        self.assertEqual(r15._Rectangle__display, '\n\n  ##\n  ##')

    def test___str__(self):
        """Task 6. __str__"""
        # Normal use: `width`, `height` initialized
        r16 = Rectangle(2, 3)
        self.assertEqual(str(r16), '[Rectangle] (1) 0/0 - 2/3')
        # Normal use: `width`, `height`, `x` initialized
        r17 = Rectangle(3, 4, 5)
        self.assertEqual(str(r17), '[Rectangle] (2) 5/0 - 3/4')
        # Normal use: `width`, `height`, `x`, `y` initialized
        r18 = Rectangle(4, 5, 6, 7)
        self.assertEqual(str(r18), '[Rectangle] (3) 6/7 - 4/5')
        # Normal use: `width`, `height`, `x`, `y`, `id` initialized
        r19 = Rectangle(5, 6, 7, 8, 4)
        self.assertEqual(str(r19), '[Rectangle] (4) 7/8 - 5/6')

    def test_update_args(self):
        """Task 8. Update #0 - *args"""
        # TypeError: 0 args (not in project instructions)
        r20 = Rectangle(2, 3)
        self.assertEqual(r20.id, 1)
        self.assertRaises(TypeError, r20.update)
        # Normal use: set `id` with 1 arg, id not in `__assigned_ids`
        r21 = Rectangle(2, 3)
        self.assertEqual(r21.id, 2)
        r21.update(89)
        self.assertEqual(r21.id, 89)
        # Normal use: set `id` w/ 1 arg, id already assigned to that instance
        self.assertEqual(r21.id, 89)
        r21.update(89)
        self.assertEqual(r21.id, 89)
        # ValueError: set `id` w/ 1 arg, id already assigned to other instance
        r22 = Rectangle(2, 3)
        self.assertEqual(r22.id, 3)
        self.assertEqual(r22.serial, 3)
        r22.update(89)
        self.assertEqual(r22.id, 89)
        self.assertEqual(r22.serial, 3)
        # Normal use: set `id`, `width` with 2 args
        r23 = Rectangle(2, 3)
        self.assertEqual(r23.id, 4)
        r23.update(90, 13)
        self.assertEqual(r23.id, 90)
        self.assertEqual(r23.width, 13)
        # Normal use: set `id`, `width`, `height` with 3 args
        r24 = Rectangle(2, 3)
        self.assertEqual(r24.id, 5)
        r24.update(91, 12, 13)
        self.assertEqual(r24.id, 91)
        self.assertEqual(r24.width, 12)
        self.assertEqual(r24.height, 13)
        # Normal use: set `id`, `width`, `height`, `x` with 4 args
        r25 = Rectangle(2, 3, 4)
        self.assertEqual(r25.id, 6)
        r25.update(92, 12, 13, 14)
        self.assertEqual(r25.id, 92)
        self.assertEqual(r25.width, 12)
        self.assertEqual(r25.height, 13)
        self.assertEqual(r25.x, 14)
        # Normal use: set `id`, `width`, `height`, `x`, `y` with 5 args
        r26 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r26.id, 7)
        r26.update(93, 12, 13, 14, 15)
        self.assertEqual(r26.id, 93)
        self.assertEqual(r26.width, 12)
        self.assertEqual(r26.height, 13)
        self.assertEqual(r26.x, 14)
        self.assertEqual(r26.y, 15)
        # TypeError: over 5 argsNormal use: set `id`, `width`, `height`, `x`,
        # `y` with 5 args (not in project instructions)
        r27 = Rectangle(4, 5, 6, 7)
        self.assertEqual(r27.id, 8)
        self.assertRaises(TypeError, r26.update, 89, 12, 13, 14, 15, 16)

    def test_update_kwargs(self):
        """Task 9. Update #1 - **kwargs"""
        # TypeError: 0 args of any type (not in project instructions)
        r28 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r28.id, 1)
        self.assertRaises(TypeError, r28.update)
        # Normal use: 1 keyword arg
        self.assertEqual(r28.id, 1)
        self.assertEqual(r28.height, 10)
        r28.update(height=1)
        self.assertEqual(r28.height, 1)
        # Normal use: multiple keyword args, none set more than once
        self.assertEqual(r28.id, 1)
        self.assertEqual(r28.width, 10)
        self.assertEqual(r28.x, 10)
        r28.update(width=1, x=2)
        self.assertEqual(r28.id, 1)
        self.assertEqual(r28.width, 1)
        self.assertEqual(r28.x, 2)
        # Normal use: multiple keyword args, some updated once already
        self.assertEqual(r28.id, 1)
        self.assertEqual(r28.y, 10)
        self.assertEqual(r28.width, 1)
        self.assertEqual(r28.x, 2)
        r28.update(y=1, width=2, x=3)
        self.assertEqual(r28.id, 1)
        self.assertEqual(r28.y, 1)
        self.assertEqual(r28.width, 2)
        self.assertEqual(r28.x, 3)
        # Normal use: multiple keyword args, including `id` not in use
        self.assertEqual(r28.id, 1)
        self.assertEqual(r28.y, 1)
        r28.update(y=2, id=89)
        self.assertEqual(r28.id, 89)
        self.assertEqual(r28.y, 2)
        # Normal use: keyword arg `id` already assigned to that same instance
        r28.update(y=2, id=89)
        self.assertEqual(r28.id, 89)
        self.assertEqual(r28.y, 2)
        # Normal use: 1 to 5 non-kwargs take precedence if before kwargs
        r29 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r29.id, 10)
        r29.update(11, 11, 11, 11, 11, x=12, height=13, y=14, width=15, id=16)
        self.assertEqual(r29.id, 11)
        self.assertEqual(r29.width, 11)
        self.assertEqual(r29.height, 11)
        self.assertEqual(r29.x, 11)
        self.assertEqual(r29.y, 11)
        # keyword arg `id` already assigned to another instance
        r30 = Rectangle(2, 3)
        self.assertEqual(r30.id, 2)
        self.assertEqual(r30.y, 0)
        r30.update(y=1, id=89)
        self.assertEqual(r30.id, 89)
        self.assertEqual(r30.y, 1)
        # KeyError: if any key not among names of `Rectangle` getters
        self.assertEqual(r30.id, 89)
        self.assertRaises(KeyError, r30.update, x=1, perimeter=2, y=3,
                          width=4)
        # SyntaxErrors cause unittest failure to import module
        """
        # SyntaxError: any mixing of args and kwargs
        r30 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r30.id, 2)
        self.assertRaises(SyntaxError, r25.update, x=1, 90, y=3, width=4)
        # SyntaxError: args and kwargs unmixed, but args appear after
        self.assertEqual(r30.id, 2)
        self.assertRaises(SyntaxError, r25.update, x=1, y=3, width=4, 90, 10)
        # SyntaxError: more than 5 keyword args/repeated key
        self.assertEqual(r28.id, 1)
        self.assertRaises(SyntaxError, r28.update, x=1, height=2, y=3,
                          width=4, id=2, x=2)
        """

    def test_to_dictionary(self):
        """13. Rectangle instance to dictionary representation"""
        # Normal use: no args
        r31 = Rectangle(5, 4, 3, 2, 10)
        self.assertEqual(r31.to_dictionary(),
                         {'id': 10, 'x': 3, 'width': 5, 'y': 2, 'height': 4})
        # TypeError: 1 or more args
        self.assertRaises(TypeError, r31.to_dictionary, 20)

    def test_to_json_string(self):
        """15. Dictionary to JSON string
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: 1 arg (list) of (dict)
        dict_list = [{'width': 10, 'x': 2, 'height': 7, 'y': 8, 'id': 1}]
        dl = Rectangle.to_json_string(dict_list)
        self.assertEqual(Rectangle.from_json_string(dl),
                         [{'id': 1, 'x': 2, 'height': 7, 'y': 8, 'width': 10}])
        # Empty list
        self.assertEqual(Base.to_json_string([]), '[]')
        # None list
        self.assertEqual(Base.to_json_string(None), '[]')
        # deprecated use: list not of dicts
        lst = [2, 3, 4]
        self.assertEqual(Base.to_json_string(lst), '[2, 3, 4]')
        # TypeError: no args
        self.assertRaises(TypeError, Base.to_json_string)
        dict_list2 = [{'width': 13, 'x': 5, 'height': 10, 'y': 11, 'id': 3}]
        # TypeError: 2+ args
        self.assertRaises(TypeError, Base.to_json_string,
                          dict_list, dict_list2)

    def test_save_to_file(self):
        """16. JSON string to file
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: list of `Rectangle` objects into JSON string file
        r32 = Rectangle(5, 6, 7, 8, 9)
        Rectangle.save_to_file([r32])
        with open('Rectangle.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(Rectangle.from_json_string(contents),
                         [{'width': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}])
        # Empty list
        Rectangle.save_to_file([])
        with open('Rectangle.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(contents, '[]')
        # None list
        Rectangle.save_to_file(None)
        with open('Rectangle.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(contents, '[]')
        # TypeError: arg not an iterable type
        self.assertRaises(TypeError, Rectangle.save_to_file, 5)
        # AttributeError: arg not a list, but tuple or set
        tup = (r32.to_dictionary(),)
        self.assertRaises(AttributeError, Rectangle.save_to_file, tup)
        # AttributeError: list contents Base, not Square or Rectangle
        b1 = Base(3)
        self.assertRaises(AttributeError, Rectangle.save_to_file, [b1])
        # TypeError: no args
        self.assertRaises(TypeError, Rectangle.save_to_file)
        # TypeError: 2+ args
        self.assertRaises(TypeError, Rectangle.save_to_file, [r32], [b1])
        # class of list objects does not match class that called save_to_file
        pass

    def test_from_json_string(self):
        """17. JSON string to dictionary
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: 1 arg (str)
        json_str = '[{"width": 5, "height": 6, "x": 7, "y": 8, "id": 9}]'
        a = Rectangle.from_json_string(json_str)
        self.assertEqual(a, [{'width': 5, 'height': 6, 'x': 7,
                              'y': 8, 'id': 9}])
        # Empty str
        b = Rectangle.from_json_string('')
        self.assertEqual(b, [])
        # None str
        c = Rectangle.from_json_string(None)
        self.assertEqual(c, [])
        # TypeError: no args
        self.assertRaises(TypeError, Rectangle.from_json_string)
        # TypeError: 2+ args
        self.assertRaises(TypeError, Rectangle.from_json_string, a, b)

    def test_create(self):
        """18. Dictionary to Instance
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: dict/keyworded args
        dic = {'width': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}
        r33 = Rectangle.create(**dic)
        self.assertTrue(type(r33) is Rectangle)
        self.assertEqual(r33.id, 9)
        self.assertEqual(r33.width, 5)
        self.assertEqual(r33.height, 6)
        self.assertEqual(r33.x, 7)
        self.assertEqual(r33.y, 8)
        # TypeError: no args
        self.assertRaises(TypeError, Rectangle.create)
        # TypeError: with fixed amount of non-keyword args
        self.assertRaises(TypeError, Rectangle.create, dic)
        # TypeError: with variable amount of non-keyword args
        self.assertRaises(TypeError, Rectangle.create, *dic)
        # KeyError: dict has bad key
        dic2 = {'area': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}
        self.assertRaises(KeyError, Rectangle.create, **dic2)
        # TypeError: dict has too many keys
        dic3 = {'area': 10, 'width': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}
        self.assertRaises(TypeError, Rectangle.create, **dic3)
        # TypeError: dict has no keys
        dic4 = dict()
        self.assertRaises(TypeError, Rectangle.create, **dic4)

    def test_load_from_file(self):
        """19. File to instances
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: file with JSON string of instances as dicts
        r33 = Rectangle(10, 7, 2, 8)
        l_in = [r33]
        Rectangle.save_to_file(l_in)
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_in[0].id, l_out[0].id)
        self.assertEqual(l_in[0].width, l_out[0].width)
        self.assertEqual(l_in[0].height, l_out[0].height)
        self.assertEqual(l_in[0].x, l_out[0].x)
        self.assertEqual(l_in[0].y, l_out[0].y)
        self.assertFalse(l_in[0] is l_out[0])
        self.assertNotEqual(l_in[0].serial, l_out[0].serial)
        # empty file returns empty list
        Rectangle.save_to_file(None)
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_out, [])
        # empty list in file returns empty list
        Rectangle.save_to_file([])
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_out, [])
        # file not found returns empty list
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')
        l_out = Rectangle.load_from_file()
        self.assertEqual(l_out, [])
        # ValueError: file has other content - JSON decoder error
        content = """It is your responsibility to request a review for this
        task from a peer before the projects deadline. If no peers have been
        reviewed, you should request a review from a TA or staff member."""
        with open('Rectangle.json', 'w', encoding='utf-8') as file:
            file.write(content)
        self.assertRaises(ValueError, Rectangle.load_from_file)
        # PermissionError: file inaccessible
        Rectangle.save_to_file(l_in)
        os.chmod('Rectangle.json', 0o000)
        self.assertRaises(PermissionError, Rectangle.load_from_file)
        # KeyError: dict has bad key
        # TypeError: dict has too many keys
        # TypeError: dict has no keys
        # mixed square and rectangle objects represented in string

if __name__ == '__main__':
    unittest.main()
