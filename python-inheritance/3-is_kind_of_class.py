#!/usr/bin/python3
"""
Este módulo contiene la función para verificar una objeto
pertenece a una clase o a heredado de una clase.
"""


def is_kind_of_class(obj, a_class):
    """
    Esta función verfirica sí un objecto es instancia de una clase.

    Args:
        obj (objeto): Objecto que se quiere verificar.

    Returns:
        True (bool): Sí es instancia, False de lo contrario.
    """
    return isinstance(obj, a_class)
