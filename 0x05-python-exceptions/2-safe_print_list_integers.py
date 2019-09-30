#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed
