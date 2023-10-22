#!/usr/bin/python3
"""
Defines a Rectangle Class
"""


class Rectangle:
    """
    Represent a rectangle
    Attributes:
        numbers_of_instance (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializable a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        type(self).number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Get/set the width of the Rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Get/set the height of the Rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Return the area of Rectangle.
        """

        return(self.__width * self.__height)

    def perimeter(self):
        """
        Return the perimeter of Rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        return "\n".join(["#" * self.__width for _ in range(self.__height)])