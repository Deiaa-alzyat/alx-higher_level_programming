#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
if digit > 5:
    p = "greater than 5"
elif digit == 0:
    p = "0"
else:
    p = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, digit, p))
