def safe_print_list(my_list=[], x=0):
    printed = 0
    for element in my_list:
        if printed < x:
            print("{}".format(element), end="")
            printed = printed + 1
    print()
    return printed
