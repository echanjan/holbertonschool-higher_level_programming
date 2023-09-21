#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    text_arg = "arguments."

    if num_args == 1:
        text_arg = "argument:"

    elif num_args > 1:
        text_arg = "arguments:"

    print("{0} {1}".format(num_args, text_arg))

    for i, arg in enumerate(args, start=1):

        print(f"{i}: {arg}")
