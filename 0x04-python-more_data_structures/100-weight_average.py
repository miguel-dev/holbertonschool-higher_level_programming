#!/usr/bin/python3


def weight_average(my_list=[]):
    product = 0
    weight_sum = 0
    length = len(my_list)
    for i in range(length):
        product += my_list[i][0] * my_list[i][1]
        weight_sum += my_list[i][1]
    return product/weight_sum
