def safe_print_list(my_list=[], x=0):
    printed = 0
    length = len(my_list)
    try:
        for element in range(1, length):
            if printed < x:
                print("{}".format(element), end="")
                printed = printed + 1
        print()
    except IndexError:
        print("List is empty.")
    return printed
