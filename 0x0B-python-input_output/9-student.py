#!/usr/bin/python3
"""Module 9-student.py"""



class Student():
    """Class that defines a student"""
    def__init__(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name

    def to_json(self):
        """retrieves a dictionary representation of a Student instance."""
        return vars(self)
