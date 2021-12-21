#!/usr/bin/python3
"""Module for append_write fnction."""




def append_write(filename="", text=""):
    """This function appends a string at the end of the text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
