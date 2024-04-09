#!/usr/bin/python3
"""Prevents the user from dynamically creating new instance attributes"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        pass
