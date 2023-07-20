#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_to_int_map = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    total = 0
    prev_value = 0

    for roman in reversed(roman_string):
        arabic = roman_to_int_map[roman]

        if arabic < prev_value:
            total -= arabic
        else:
            total += arabic

        prev_value = arabic

    return total
