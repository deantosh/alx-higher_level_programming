#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is 0 and is 0")
else:
    if number < 0:
        digit = -1 * ((number * -1) % 10)
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
