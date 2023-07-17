#!/usr/bin/python3

def max_integer(my_list=[]):
     
    if len(my_list) == 0:
        return (None)

    else:
        biggest_int = my_list[0]

        for a in range(len(my_list)):
        if my_list[a] > biggest_int:
            biggest_int = my_list[a]

    return (biggest_int)
