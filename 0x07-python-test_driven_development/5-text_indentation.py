#!/usr/bin/python3

""" prints a text with 2 new lines after each of these characters:
    ., ? and :
"""


def text_indentation(text):
    """
    This function takes in a string of text and adds indentation to it.

    Args:
        text (str): The input text to be indented.

    Returns:
        None

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    token_list = []
    count = 0
    tracker = 0

    for i in text:
        if i in [".", "?", ":"]:
            count += 1

    for i in range(count):
        token = ""
        for j in text:
            tracker += 1
            if j not in [".", "?", ":"]:
                token += j
            else:
                token += j + "\n\n"
                token_list.append(token.strip())
                text = text[tracker:]
                tracker = 0
                break

    for i in token_list:
        print(f"{i}\n")
