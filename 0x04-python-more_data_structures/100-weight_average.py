#!/usr/bin/python3
def weight_average(my_list=[]):
    # returns the weighted average of all integers tuple (<score>, <weight>)
    if my_list is None or len(my_list) == 0:
        return 0

    tup_prod_sum = 0
    weight_sum = 0

    for i in my_list:
        # add the product of each tuple to variable
        tup_prod_sum += i[0] * i[1]
        # add the weights of each tuple to variable
        weight_sum += i[1]

    return (tup_prod_sum / weight_sum)
