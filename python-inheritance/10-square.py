#!/usr/bin/python3
"""
Este modulo define una clase vacia.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Esta clase define un Square que hereda de Rectangle.
    """

    def __init__(self, size):
        """
        Método constructor que recibe el tamaño.

        Args:
            size (int): Tamaño de nuestra clas Square
        """

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Este método cálcula el área de nuestra cuadrado.

        Returns:
            int : size * 2
        """
        return self.__size

    def __str__(self):
        """
        Este método regresa una cadena informal de nuestra clase.

        Returns:
            string: Representación informal de Square.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
