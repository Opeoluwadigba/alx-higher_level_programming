#!/usr/bin/python3
"""
Module 8-rectangle
Contains parent class BaseGeometry
with public instance method area and integer_validator
Contains subclass Rectangle
with instantiation of private attributes length and breadth, validated by parent
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry
    Methods:
        __init__(self, length, and breadth)
    """
    def __init__(self, width, height):
        """validate and initialize length and breadth
        Args:
            length (int): private
            breadth (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
