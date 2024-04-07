#!/usr/bin/python3
"""
Module processes a text and create a new text and a newline after each
separator is found (.:?).
"""


def text_indentation(text):
    """returns: prints a text with 2 new lines"""

    # validate input
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    modified_text = text.replace('.', '.\n').replace(':', ':\n').replace('?', '?\n')
    lines = modified_text.splitlines()

    size = len(lines)
    count = 0
    for line in lines:
        stripped_line = line.strip()

        count += 1
        if count < size:
            print(stripped_line + "\n")
        else:
            print(stripped_line, end="")
