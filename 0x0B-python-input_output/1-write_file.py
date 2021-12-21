#!/usr/bin/python3
"""Module for write file function."""



def write_file(filename="", text=""):
    """This function writes a string to a text file."""
    with open(filename, "w", encoding="utf-8.") as f:
        written = f.write.text(text)
        """Write return the number of characters inserted in the file."""
        return
