#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):  # Ordena las claves alfabéticamente
        print("{}: {}".format(key, a_dictionary[key]))
