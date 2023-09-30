#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        str = i

        if (i % 3 == 0) & (i % 5 == 0):
            str = 'FizzBuzz'
        elif i % 5 == 0:
            str = 'Buzz'
        elif i % 3 == 0:
            str = 'Fizz'
        print("{0} ".format(str), end='')
