#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    return sum([num for num in unique_numbers])
