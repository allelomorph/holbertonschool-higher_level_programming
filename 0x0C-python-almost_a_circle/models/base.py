#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 1, 15-19"""
import json


class Base:
    """Assigns `id` and manages related attributes across all instances.

    Assigns valid id from arg, or without an arg the current count of
    instances, `__nb_objects`. Added features not in project instructions:
    `__assigned_ids` (set) of (int): set of all ids assigned at least once
    `__serial` (int) + getter/setter: `__nb_objects` after self.__init__, does
    not change even if `id` does

    Args:
        id (int): identifying number for each instance of cls, may be assigned
            to multiple instances

    Attributes:
        __nb_objects (int): number of `Base` instances not assigned id at
            initialization
        __true_nb_objects (int): total all of `Base` instances
        __assigned_ids (set) of (ints): set of all `id` numbers assigned at
            least once

    Project tasks:
        1. Base class - /models, __init__.py, class Base, __init__

    """
    __nb_objects = 0
    __true_nb_objects = 0
    __assigned_ids = set()

    def __init__(self, id=None):
        if id is not None:
            # init with custom id, or reassignment from update()
            self.id = id
            # true total up and serial set only after id validated
            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)
        else:
            # per project instructions, __nb_objects up only with no id arg
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            # update true total, serial and assigned id set
            Base.__true_nb_objects += 1
            self.serial = Base.__true_nb_objects
            Base.__assigned_ids.add(self.id)

    @property
    def id(self):
        """Getter for `id`

        Returns:
            __id (int): unique identifer for each instance of cls

        """
        return self.__id

    @id.setter
    def id(self, value):
        """Args:
            value (int): number to be assigned as id

        Attributes:
            __id (int): unique identifer for each instance of cls

        Raises:
            ValueError: if `id` arg is 0, negative, or already assigned.

        """
        if value < 1:
            raise ValueError('id must be positive')
        self.__id = value

    @property
    def serial(self):
        """Getter for `serial`

        Returns:
            __serial (int): unique identifer for each instance of cls, taken
                from __true_nb_objects at time of instantiation

        """
        return self.__serial

    @serial.setter
    def serial(self, value):
        """Args:
            value (int): number to be assigned as `serial`

        Attributes:
            __serial (int): unique identifer for each instance of cls, taken
                from __true_nb_objects at time of instantiation
        """
        self.__serial = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries into JSON string.

        Args:
            list_dictionaries (list) of (dict): list to be converted

        Returns:
            JSON format string of `list_dictionaries`, or '[]' if None or
                empty

        Project tasks:
            15. Dictionary to JSON string - static method `to_json_string()`
                 that returns the JSON string representation of
                 list_dictionaries, or [] if None

        """
        if list_dictionaries is None or list_dictionaries == []:  # len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves to file a JSON formatted string of a list of dictionary
        representations of objects of `Base` derived classes.

        Args:
            list_objs (list) of (dict): list of `Base` derived objects (in
                this project `Rectangle` and `Square`)

        Project tasks:
            16. JSON string to file - class method `save_to_file()` that writes
                the JSON string representation of `list_objs` to a file, using
                `to_json_string()`, overwriting existing file, class name in
                filename, if list None then list = []

        """
        if list_objs is None:
            list_objs = []

        list_dicts = []
        for item in list_objs:
            list_dicts.append(item.to_dictionary())
        json_dict = cls.to_json_string(list_dicts)

        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of objects represented by JSON format string,
        or [] if `json_string` is None or empty

        Args:
            json_string (str): JSON format string to be converted

        Returns:
            List of objects represented by JSON format string, or [] if
                `json_string` is None or empty

        Project tasks:
            17. JSON string to dictionary - static method `from_json_string()`
                that returns the list of the JSON string representation
                `json_string`, a string representing a list of dictionaries,
                or if None or empty, return an empty list

        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new dummy instance of class and `update()`s it using
        `dictionary` as keyword args

        Args:
            dictionary (dict): dictionary to be used as keyword args

        Project tasks:
            18. Dictionary to Instance - class method `create()` that creates
                a new dummy instance and `update()`s it with values in
                `dictionary` as keyword args

        """
        if cls.__name__ is 'Rectangle':
            temp = cls(1, 1)
        elif cls.__name__ is 'Square':
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Returns list of instances from file <class name>.json, or empty list
        if no file. `cls` determines class of instances.

        Returns:
            list of instances of `cls` from file <class name>.json, or empty
                list if no file

        Project tasks:
            19. File to instances - class method `load_from_file()` returns
                list of instances from file <Class name>.json, or empty list
                if no file. must use `from_json_string()` and `create()`,
                class of instances in list depends on cls

        """
        import os.path

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
        else:
            return []
        obj_list = cls.from_json_string(json_str)
        instance_list = []
        for item in obj_list:
            instance_list.append(cls.create(**item))
        return instance_list
