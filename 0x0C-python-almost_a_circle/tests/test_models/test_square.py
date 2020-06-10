#!/usr/bin/python3
"""Unittest for Square([..]) to task 14, and inheritance for 15-19

# with `unittest discover` the functions are run in alpha order by name of
class, then func name.

"""
import unittest
import contextlib  # for redirecting stdout during print tests
import os  # for tearDownClass and test_load_from_file
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests `Square` class, subclass of `Rectangle`, itself of `Base`.

    """
    @classmethod
    def setUpClass(cls):
        """Alerts user to any instances of tested classes or subclasses not
        already cleaned up.

        """
        s_obj = Base._Base__nb_objects
        s_ids = Base._Base__assigned_ids
        if s_obj > 1:
            print('TestSquare: caution: Base counter not reset,' +
                  ' now at: {}'.format(s_obj))
        if len(s_ids) > 0:
            print('TestSquare: caution: Base ids still in use:' +
                  ' {}'.format(s_ids))

    def tearDown(self):
        """Reinitializes `Square` space `Base` obejct iterator and set of
        assigned ids.

        """
        if os.path.exists('Square.json'):
            os.remove('Square.json')
        Square._Base__nb_objects = 0
        Square._Base__assigned_ids.clear()
        Base._Base__nb_objects = 0
        Base._Base__assigned_ids.clear()
        s_obj = Base._Base__nb_objects
        s_ids = Base._Base__assigned_ids
        if s_obj > 1:
            print('TestSquare: caution: counter not reset,' +
                  ' now at: {}'.format(s_obj))
        if len(s_ids) > 0:
            print('TestSquare: caution: ids still in use: {}'.format(s_ids))

    def test_arg_count(self):
        """Task 10. And now, the Square!"""
        # TypeError: 0 args
        self.assertRaises(TypeError, Square)
        # Normal use: 1 arg - x, `y default to 0, id defaults to serial
        s1 = Square(3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.serial, 1)
        # Normal use: 2 args - y defaults to 0, id defaults to serial
        s2 = Square(3, 3)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.serial, 2)
        # Normal use: 3 args - id defaults to serial
        s3 = Square(2, 2, 2)
        self.assertEqual(s3.size, 2)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 2)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s3.serial, 3)
        # Normal use: 4 args - no defaults
        s4 = Square(3, 3, 3, 10)
        self.assertEqual(s4.size, 3)
        self.assertEqual(s4.x, 3)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 10)
        # TypeError: over 4 args
        self.assertRaises(TypeError, Square, 3, 3, 3, 3, 3)

    def test_id_value(self):
        """10. And now, the Square!
        Testing inheritance of validation from `Base` via `Rectangle`

        """
        # no id arg, id defualts to serial
        s5 = Square(2)
        self.assertEqual(s5.id, 1)
        self.assertEqual(s5.serial, 1)
        # Normal use: id arg assigned via arg
        s6 = Square(2, 2, 2, 10)
        self.assertEqual(s6.id, 10)
        # id arg is 0
        self.assertRaises(ValueError, Square, 1, 1, 1, 0)
        # id arg less than 0
        self.assertRaises(ValueError, Square, 1, 1, 1, -2)
        # id arg already assigned to another instance of `Square` family
        s7 = Square(1, 1, 1, 2)
        self.assertEqual(s7.id, 2)
        self.assertEqual(s7.serial, 3)

    def test_size_derivation(self):
        """11. Square size
        Illustrates relationship of `size` to `width` and `height`

        """
        s8 = Square(2)
        # AttributeError raised by unittest before testing
        """
        # `size` does not exist as its own attribute:
        self.assertEqual(s5.id, 1)
        self.assertRaises(AttributeError, s5._Square__size)
        """
        # but instead has getter referencing width
        self.assertEqual(s8.width, 2)
        self.assertEqual(s8.size, 2)
        s8._Rectangle__width = 3
        self.assertEqual(s8.size, 3)
        # and setter that changes width and height
        self.assertEqual(s8.id, 1)
        self.assertEqual(s8.width, 3)
        self.assertEqual(s8.height, 2)
        self.assertEqual(s8.size, 3)
        s8.size = 5
        self.assertEqual(s8.id, 1)
        self.assertEqual(s8.width, 5)
        self.assertEqual(s8.height, 5)
        self.assertEqual(s8.size, 5)

    def test_size_value(self):
        """11. Square size
        Equivalent to `test_width_value()` from `test_rectangle`, here
        testing inheritance of validation from `Rectangle`

        """
        # Normal use: size is int > 0, self.width and self.height set to same
        s9 = Square(3)
        self.assertEqual(s9.id, 1)
        self.assertEqual(s9.size, 3)
        self.assertEqual(s9.width, 3)
        self.assertEqual(s9.height, 3)
        # ValueError: size is int 0
        self.assertRaises(ValueError, Square, 0)
        # ValueError size is int < 0
        self.assertRaises(ValueError, Square, -3)
        # TypeError: size is float
        self.assertRaises(TypeError, Square, 3.0)
        # TypeError: size is str
        self.assertRaises(TypeError, Square, '3')
        # TypeError: size is tuple
        self.assertRaises(TypeError, Square, (3,))
        # TypeError: size is list
        self.assertRaises(TypeError, Square, [3])
        # TypeError: size is bool
        self.assertRaises(TypeError, Square, True)
        # TypeError: size is set
        self.assertRaises(TypeError, Square, {3, 4})
        # TypeError: size is None
        self.assertRaises(TypeError, Square, None)

    def test_x_value(self):
        """10. And now, the Square!
        Equivalent to `test_x_value()` from `test_rectangle`, here testing
        inheritance of validation from `Rectangle`

        """
        # Normal use: x is int > 0
        s10 = Square(3, 3)
        self.assertEqual(s10.id, 1)
        self.assertEqual(s10.x, 3)
        # Normal use: x is int 0
        s11 = Square(3, 0)
        self.assertEqual(s11.id, 2)
        self.assertEqual(s11.x, 0)
        # ValueError: x is int < 0
        self.assertRaises(ValueError, Square, 3, -3)
        # TypeError: x is float
        self.assertRaises(TypeError, Square, 3, 3.0)
        # TypeError: x is str
        self.assertRaises(TypeError, Square, 3, '3')
        # TypeError: x is tuple
        self.assertRaises(TypeError, Square, 3, (3,))
        # TypeError: x is list
        self.assertRaises(TypeError, Square, 3, [3])
        # TypeError: x is bool
        self.assertRaises(TypeError, Square, 3, True)
        # TypeError: x is set
        self.assertRaises(TypeError, Square, 3, {3, 4})
        # TypeError: x is None
        self.assertRaises(TypeError, Square, 3, None)

    def test_y_value(self):
        """10. And now, the Square!
        Equivalent to `test_y_value()` from `test_rectangle`, here testing
        inheritance of validation from `Rectangle`

        """
        # Normal use: y is int > 0
        s12 = Square(3, 1, 3)
        self.assertEqual(s12.id, 1)
        self.assertEqual(s12.y, 3)
        # Normal use: y is int 0
        s13 = Square(3, 1, 0)
        self.assertEqual(s13.id, 2)
        self.assertEqual(s13.y, 0)
        # ValueError: y is int < 0
        self.assertRaises(ValueError, Square, 3, 3, -3)
        # TypeError: y is float
        self.assertRaises(TypeError, Square, 3, 3, 3.0)
        # TypeError: y is str
        self.assertRaises(TypeError, Square, 3, 3, '3')
        # TypeError: y is tuple
        self.assertRaises(TypeError, Square, 3, 3, (3,))
        # TypeError: y is list
        self.assertRaises(TypeError, Square, 3, 3, [3])
        # TypeError: y is bool
        self.assertRaises(TypeError, Square, 3, 3, True)
        # TypeError: y is set
        self.assertRaises(TypeError, Square, 3, 3, {3, 4})
        # TypeError: y is None
        self.assertRaises(TypeError, Square, 3, 3, None)

    def test___str__(self):
        """10. And now, the Square!
        String output: '[Square] (<id>) <x>/<y> - <size>'

        """
        # Normal use: 1 arg, default `x`, `y`, `id`
        s14 = Square(2)
        self.assertEqual(str(s14), '[Square] (1) 0/0 - 2')
        # Normal use: 2 args, default `y`, `id`
        s15 = Square(3, 4)
        self.assertEqual(str(s15), '[Square] (2) 4/0 - 3')
        # Normal use: 3 args, default `id`
        s16 = Square(5, 6, 7)
        self.assertEqual(str(s16), '[Square] (3) 6/7 - 5')
        # Normal use: 4 args, no defaults
        s17 = Square(8, 9, 10, 11)
        self.assertEqual(str(s17), '[Square] (11) 9/10 - 8')

    def test_update_args(self):
        """12. Square update
        Testing non-keyword variable args for `Square.update()`

        """
        # TypeError: 0 args (not in project instructions)
        s18 = Square(2)
        self.assertEqual(s18.id, 1)
        self.assertRaises(TypeError, s18.update)
        # Normal use: set `id` with 1 arg, id not in `__assigned_ids`
        s19 = Square(2)
        self.assertEqual(s19.id, 2)
        s19.update(89)
        self.assertEqual(s19.id, 89)
        # Normal use: set `id` w/ 1 arg, id already assigned to that instance
        self.assertEqual(s19.id, 89)
        s19.update(89)
        self.assertEqual(s19.id, 89)
        # ValueError: set `id` w/ 1 arg, id already assigned to other instance
        s20 = Square(2)
        self.assertEqual(s20.id, 3)
        s20.update(89)
        self.assertEqual(s20.id, 89)
        self.assertEqual(s20.serial, 3)
        # Normal use: set `id`, `size` with 2 args
        s21 = Square(4)
        self.assertEqual(s21.id, 4)
        self.assertEqual(s21.size, 4)
        s21.update(90, 14)  # id 3 can be reused
        self.assertEqual(s21.id, 90)
        self.assertEqual(s21.size, 14)
        # Normal use: set `id`, `width`, `x` with 3 args
        s22 = Square(5, 6)
        self.assertEqual(s22.id, 5)
        self.assertEqual(s22.size, 5)
        self.assertEqual(s22.x, 6)
        s22.update(91, 15, 16)  # id 3 can be reused
        self.assertEqual(s22.id, 91)
        self.assertEqual(s22.size, 15)
        self.assertEqual(s22.x, 16)
        # Normal use: set `id`, `width`, `x`, `y` with 4 args
        s23 = Square(5, 6, 7, 4)
        self.assertEqual(s23.id, 4)
        self.assertEqual(s23.size, 5)
        self.assertEqual(s23.x, 6)
        self.assertEqual(s23.y, 7)
        s23.update(92, 15, 16, 17)  # id 4 can be reused
        self.assertEqual(s23.id, 92)
        self.assertEqual(s23.size, 15)
        self.assertEqual(s23.x, 16)
        self.assertEqual(s23.y, 17)
        # TypeError: over 4 args (not in project instructions)
        s24 = Square(6, 7, 8, 5)
        self.assertEqual(s24.id, 5)
        self.assertRaises(TypeError, s24.update, 89, 12, 13, 14, 15)

    def test_update_kwargs(self):
        """12. Square update
        Testing keyword args for `Square.update()`

        """
        # TypeError: 0 args of any type (not in project instructions)
        s25 = Square(1, 1, 1, 1)
        self.assertEqual(s25.id, 1)
        self.assertRaises(TypeError, s25.update)
        # Normal use: 1 keyword arg
        self.assertEqual(s25.id, 1)
        self.assertEqual(s25.x, 1)
        s25.update(x=3)
        self.assertEqual(s25.x, 3)
        # Normal use: multiple keyword args, none set more than once
        self.assertEqual(s25.id, 1)
        self.assertEqual(s25.size, 1)
        self.assertEqual(s25.y, 1)
        s25.update(y=4, size=5)
        self.assertEqual(s25.id, 1)
        self.assertEqual(s25.size, 5)
        self.assertEqual(s25.y, 4)
        # Normal use: multiple keyword args, some updated once already
        self.assertEqual(s25.id, 1)
        self.assertEqual(s25.size, 5)
        self.assertEqual(s25.x, 3)
        self.assertEqual(s25.y, 4)
        s25.update(y=6, size=7, x=8)
        self.assertEqual(s25.id, 1)
        self.assertEqual(s25.size, 7)
        self.assertEqual(s25.x, 8)
        self.assertEqual(s25.y, 6)
        # Normal use: multiple keyword args, including `id` not in use
        self.assertEqual(s25.id, 1)
        self.assertEqual(s25.y, 6)
        s25.update(y=2, id=89)
        self.assertEqual(s25.id, 89)
        self.assertEqual(s25.y, 2)
        # Normal use: keyword arg `id` already assigned to that same instance
        self.assertEqual(s25.id, 89)
        self.assertEqual(s25.x, 8)
        s25.update(x=2, id=89)
        self.assertEqual(s25.id, 89)
        self.assertEqual(s25.x, 2)
        # Normal use: 1 to 4 non-kwargs take precedence if before kwargs
        s26 = Square(10, 10, 10, 10)
        self.assertEqual(s26.id, 10)
        self.assertEqual(s26.serial, 2)
        s26.update(11, 11, 11, 11, x=12, y=14, size=15, id=16)
        self.assertEqual(s26.id, 11)
        self.assertEqual(s26.size, 11)
        self.assertEqual(s26.x, 11)
        self.assertEqual(s26.y, 11)
        # ValueError: keyword arg `id` already assigned to another instance
        s27 = Square(2, 3)
        self.assertEqual(s27.id, 3)
        self.assertEqual(s27.serial, 3)
        s27.update(y=1, id=89)
        self.assertEqual(s27.id, 89)
        self.assertEqual(s27.serial, 3)
        # KeyError: if any key not among `size`, `x`, `y`, `id`
        self.assertEqual(s27.id, 89)
        self.assertRaises(KeyError, s27.update, x=1, perimeter=2, y=3)

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
        """14. Square instance to dictionary representation"""
        # Normal use: no args
        s28 = Square(5, 4, 3, 10)
        self.assertEqual(s28.to_dictionary(),
                         {'y': 3, 'id': 10, 'size': 5, 'x': 4})
        # TypeError: 1 or more args
        self.assertRaises(TypeError, s28.to_dictionary, 20)

    def test_to_json_string(self):
        """15. Dictionary to JSON string
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: 1 arg (list) of (dict)
        dict_list = [{'size': 10, 'x': 2, 'y': 8, 'id': 1}]
        dl = Square.to_json_string(dict_list)
        self.assertEqual(Square.from_json_string(dl),
                         [{'id': 1, 'x': 2, 'y': 8, 'size': 10}])
        # Empty list
        self.assertEqual(Square.to_json_string([]), '[]')
        # None list
        self.assertEqual(Square.to_json_string(None), '[]')
        # deprecated use: list not of dicts
        lst = [2, 3, 4]
        self.assertEqual(Square.to_json_string(lst), '[2, 3, 4]')
        # TypeError: no args
        self.assertRaises(TypeError, Square.to_json_string)
        dict_list2 = [{'size': 13, 'x': 5, 'y': 11, 'id': 3}]
        # TypeError: 2+ args
        self.assertRaises(TypeError, Square.to_json_string,
                          dict_list, dict_list2)

    def test_save_to_file(self):
        """16. JSON string to file
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: list of `Square` objects into JSON string file
        s28 = Square(6, 7, 8, 9)
        Square.save_to_file([s28])
        with open('Square.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(Square.from_json_string(contents),
                         [{'size': 6, 'x': 7, 'y': 8, 'id': 9}])
        # Empty list
        Square.save_to_file([])
        with open('Square.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(contents, '[]')
        # None list
        Square.save_to_file(None)
        with open('Square.json', encoding='utf-8') as file:
            contents = file.read()
        self.assertEqual(contents, '[]')
        # TypeError: arg not an iterable type
        self.assertRaises(TypeError, Square.save_to_file, 5)
        # AttributeError: arg not a list, but tuple or set
        tup = (s28.to_dictionary(),)
        self.assertRaises(AttributeError, Square.save_to_file, tup)
        # AttributeError: list contents Base, not Square or Rectangle
        b1 = Base(3)
        self.assertRaises(AttributeError, Square.save_to_file, [b1])
        # TypeError: no args
        self.assertRaises(TypeError, Square.save_to_file)
        # TypeError: 2+ args
        self.assertRaises(TypeError, Square.save_to_file, [s28], [b1])
        # class of list objects does not match class that called save_to_file
        pass

    def test_from_json_string(self):
        """17. JSON string to dictionary
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: 1 arg (str)
        json_str = '[{"size": 6, "x": 7, "y": 8, "id": 9}]'
        a = Square.from_json_string(json_str)
        self.assertEqual(a, [{'size': 6, 'x': 7, 'y': 8, 'id': 9}])
        # Empty str
        b = Square.from_json_string('')
        self.assertEqual(b, [])
        # None str
        c = Square.from_json_string(None)
        self.assertEqual(c, [])
        # TypeError: no args
        self.assertRaises(TypeError, Square.from_json_string)
        # TypeError: 2+ args
        self.assertRaises(TypeError, Square.from_json_string, a, b)

    def test_create(self):
        """18. Dictionary to Instance
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: dict/keyworded args
        dic = {'size': 6, 'x': 7, 'y': 8, 'id': 9}
        s29 = Square.create(**dic)
        self.assertTrue(type(s29) is Square)
        self.assertEqual(s29.id, 9)
        self.assertEqual(s29.size, 6)
        self.assertEqual(s29.x, 7)
        self.assertEqual(s29.y, 8)
        # TypeError: no args
        self.assertRaises(TypeError, Square.create)
        # TypeError: with fixed amount of non-keyword args
        self.assertRaises(TypeError, Square.create, dic)
        # TypeError: with variable amount of non-keyword args
        self.assertRaises(TypeError, Square.create, *dic)
        # KeyError: dict has bad key
        dic2 = {'area': 5, 'size': 6, 'y': 8, 'id': 9}
        self.assertRaises(KeyError, Square.create, **dic2)
        # TypeError: dict has too many keys
        dic3 = {'size': 10, 'width': 5, 'height': 6, 'x': 7, 'y': 8, 'id': 9}
        self.assertRaises(TypeError, Square.create, **dic3)
        # TypeError: dict has no keys
        dic4 = dict()
        self.assertRaises(TypeError, Square.create, **dic4)

    def test_load_from_file(self):
        """19. File to instances
        definition in `Base`, but tested here for inheritance.

        """
        # Normal use: file with JSON string of instances as dicts
        s30 = Square(10, 7, 2, 8)
        l_in = [s30]
        Square.save_to_file(l_in)
        l_out = Square.load_from_file()
        self.assertEqual(l_in[0].id, l_out[0].id)
        self.assertEqual(l_in[0].size, l_out[0].size)
        self.assertEqual(l_in[0].x, l_out[0].x)
        self.assertEqual(l_in[0].y, l_out[0].y)
        self.assertFalse(l_in[0] is l_out[0])
        self.assertNotEqual(l_in[0].serial, l_out[0].serial)
        # empty file
        Square.save_to_file(None)
        l_out = Square.load_from_file()
        self.assertEqual(l_out, [])
        # empty list in file
        Square.save_to_file([])
        l_out = Square.load_from_file()
        self.assertEqual(l_out, [])
        # file has other content - JSON decoder error
        content = """It is your responsibility to request a review for this
        task from a peer before the projects deadline. If no peers have been
        reviewed, you should request a review from a TA or staff member."""
        with open('Square.json', 'w', encoding='utf-8') as file:
            file.write(content)
        self.assertRaises(ValueError, Square.load_from_file)
        # PermissionError: file inaccessible
        Square.save_to_file(l_in)
        os.chmod('Square.json', 0o000)
        self.assertRaises(PermissionError, Square.load_from_file)
        # FileNotFoundError: file not in path
        if os.path.exists('Square.json'):
            os.remove('Square.json')
        self.assertRaises(FileNotFoundError, Square.load_from_file)
        # KeyError: dict has bad key
        # TypeError: dict has too many keys
        # TypeError: dict has no keys
        # mixed square and rectangle objects represented in string

if __name__ == '__main__':
    unittest.main()
