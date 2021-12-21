#!/usr/bin/python3
"""
Contains function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename -> name of file to write to
    """

    with open(filename, "r") as file:
        return json.load(file)
