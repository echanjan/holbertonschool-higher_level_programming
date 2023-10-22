#!/usr/bin/python3
"""
Este módulo contiene la función para validar el tipo de dato
"""


def is_same_class(obj, a_class):
    """
    Esta función verifica si un objeto es un tipo de dato en concreto.

    Args:
        obj (objeto): El objeto que se desea validar.

    Returns:
        True (bool): Sí es el mismo tipo de dato de a_class, False caso contrario.
    """
    return type(obj) == a_class
