def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for element in range(0, x):
            if printed <= x:
                print("{}".format(my_list[element]), end="")
                printed = printed + 1
        print()
    except IndexError:
        print()
        pass
    return printed
