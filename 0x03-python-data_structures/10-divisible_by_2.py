#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    multiples = []
    for each_number in my_list:
        if each_number % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
