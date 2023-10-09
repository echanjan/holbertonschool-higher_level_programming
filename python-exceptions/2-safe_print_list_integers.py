#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_element = 0

    try:
        for e in range(x):
            e = my_list[e]
            if type(e) == int:
                print("{:d}".format(e), end='')
                n_element += 1
    except IndexError as e:
        print(e)
    print()
    return n_element
