#!/usr/bin/python3
"""
Este modulo define una clase vacia.
"""


"""Importa la clase BaseGeometry del módulo 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Esta clase define un Rectangle
    """

    def __init__(self, width, height):
        """
        Este metodo inicializa con el ancho y alto del rectangulo

        Args:
            width (int): Ancho del rectangulo.
            height (int): Alto del rectangulo.
        """
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Esta función calcula el area de un rectangulo.

        Returns:
            int : ancho * alto
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Este método regresa una cadena informal de nuestra clase.

        Returns:
            string: Representación informal de Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
