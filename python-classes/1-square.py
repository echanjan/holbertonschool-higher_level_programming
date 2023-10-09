#!/usr/bin/python3
"""
Este módulo representa la clase Square
"""

class Square:
    """
    Esta clase define un cuadrado
    """

    def __init__(self, size):
        """
        Este es el constructor de la clase Square.
        Inicializa un nuevo objeto Square con el size recibido.

        Args:
        size (int o float): La longitud de los lados del square.
        """
        self.__size = size
