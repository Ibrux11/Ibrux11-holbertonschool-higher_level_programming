#!/usr/bin/python3
"""
Module for checking class inheritance.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance 
    of a class that inherited from, the specified class.

    Parameters:
    obj: Any type
        The object to be checked.
    a_class: type
        The class to compare the object against.

    Returns:
    bool
        True if the object is an instance of a_class or an instance
        of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class