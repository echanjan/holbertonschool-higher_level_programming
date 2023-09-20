#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Obtenemos los argumentos de la línea de comandos
    suma = sum(int(arg) for arg in args)

    print(suma)
