#!/usr/bin/python3
"""
Module defines ``Base`` class whic will be the parent class for all other
classes in this project.

Requirements:
 - private class attribute __nb_objects = 0
 - class constructor: def __init__(self, id=None)::
 - if id is not None, assign the public instance attribute id with this
   argument value - you can assume id is an integer and you don’t need
   to test the type of it
 - otherwise, increment __nb_objects and assign the new value to the
   public instance attribute id
 - Update the class Base by adding the static method def to_json_string(
   list_dictionaries): that returns the JSON string representation of
   list_dictionaries:
      -> list_dictionaries is a list of dictionaries
      -> If list_dictionaries is None or empty, return the string: "[]"
      -> Otherwise, return the JSON string representation of list_
         dictionaries
 - Update the class Base by adding the class method def save_to_file(
   cls, list_objs): that writes the JSON string representation of
   list_objs to a file:
      -> list_objs is a list of instances who inherits of Base - example
         : list of Rectangle or list of Square instances
      -> If list_objs is None, save an empty list
      -> The filename must be: <Class name>.json - example: Rectangle.json
      -> You must use the static method to_json_string (created before)
      -> You must overwrite the file if it already exists
 - Update the class Base by adding the static method def from_json_string
   (json_string): that returns the list of the JSON string representation
   json_string:
      -> json_string is a string representing a list of dictionaries
      -> If json_string is None or empty, return an empty list
      -> Otherwise, return the list represented by json_string
 - Update the class Base by adding the class method def create(cls,
   **dictionary): that returns an instance with all attributes already set:
      -> **dictionary can be thought of as a double pointer to a dictionary
      -> To use the update method to assign all attributes, you must create
         a “dummy” instance before:
          x. Create a Rectangle or Square instance with “dummy” mandatory
             attributes (width, height, size, etc.)
          x. Call update instance method to this “dummy” instance to apply
             your real values
      -> You must use the method def update(self, *args, **kwargs)
      -> **dictionary must be used as **kwargs of the method update
      -> You are not allowed to use eval
"""
import json


class Base:
    """defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns: a JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        json_list = []
        for dict in list_dictionaries:
            try:
                json_list.append(json.dumps(dict))
            except TypeError:
                pass
        return '[' + ", ".join(json_list) + ']'

    @staticmethod
    def from_json_string(json_string):
        """returns: an object dictionary from a json string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """returns: JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"

        # create list of dictionaries from list of object
        list_dictionaries = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            list_dictionaries.append(obj_dict)

        # get the JSON string
        json_str = Base.to_json_string(list_dictionaries)
        with open(filename, 'w') as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """returns an object with all attributes already set"""
        # create dummy object
        obj = cls(3, 5, 2)
        # call update to pass real values
        obj.update(**dictionary)
        return obj
