#!/usr/bin/python3
"""
Este modulo define una función para ver
los métodos y propiedades de una objeto.
"""


def lookup(obj):
    """
    Esta función regresa una lista con los
    métodos y propiedades.

    Args:
        obj (object): Un objeto cualquiera de Python

    Returns:
        list (list): Regresa una lista con métodos y propiedades
    """

    return dir(obj)
