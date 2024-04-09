#!/usr/bin/python3
"""Prevents the user from dynamically creating new instance attributes"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes

    """
    __slots__ = ['first_name']

    def __init__(self):
        pass
