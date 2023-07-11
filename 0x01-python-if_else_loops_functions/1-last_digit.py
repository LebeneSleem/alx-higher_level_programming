#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of" + "{number:d}"
str2 = "is" + " " + "{number[-1]" + " "

if number[-1] > 5:
    print("str1 + str2 + and is greater than 5")
elif number[-1] == 0:
    print("str1 + str2 + and is 0")
elif number[-1] < 6 and != 0:
    print("str1 + str2 + and is less than 6 and not 0")
