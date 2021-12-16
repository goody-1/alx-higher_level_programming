#!/usr/bin/python3
"""
The "text_indentation" Module.
This module contains a function that prints modified text

For example,

>>> text_indentation("Hello Duncan. How do you like your new hair!")
Hello Duncan.
<BLANKLINE>
How do you like your new hair!

But it uses the helper functions:
    strip_list(text_list) and add_delimeter(text_lilst, delimeter)
"""


def strip_list(text_list):
    """
    A helper function for 'text_indentation' function
    Takes a list of strings and strips the strings of excess white spaces
        if they exist
    Return:
        a new list of stripped strings

    Example:
        >>> strip_list([" come", " and ", "go "])
        ['come', 'and ', 'go ']
    """
    new_list = []
    for string in text_list:
        new_list.append(string.lstrip(" "))

    return new_list


def add_delimeter(text_list, delimeter):
    """
    A helper function for 'text_indentation' function

    Args:
        text_list: the list of strings to be converted
        delimeter: adding the delimeter back
    Return:
        a new_list of converted strings

    Example:
        # noqa
        >>> add_delimeter(["Gabriel is going to Vernice",
        ... "He is taking Conice with him ", " Did he inform you?"], '.')
        ['Gabriel is going to Vernice.', 'He is taking Conice with him .', ' Did he inform you?']
    """

    new_list = []
    for i in range(len(text_list) - 1):
        new_list.append(text_list[i] + delimeter)
    new_list.append(text_list[-1])

    return new_list


def text_indentation(text=""):
    """
    Prints text with 2 new lines after each of these characters: {., ? and :}
    Return:
        None
    Args:
        text - the text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    period_split = text.split('.')
    period_split = add_delimeter(period_split, '.')
    period_split = strip_list(period_split)
    period_split = '\n\n'.join(period_split)

    qmark_split = period_split.split('?')
    qmark_split = add_delimeter(qmark_split, '?')
    qmark_split = strip_list(qmark_split)
    qmark_split = '\n\n'.join(qmark_split)

    final_split = qmark_split.split(':')
    final_split = add_delimeter(final_split, ':')
    final_split = strip_list(final_split)
    final_split = '\n\n'.join(final_split)

    print("{}".format(final_split), end="")
