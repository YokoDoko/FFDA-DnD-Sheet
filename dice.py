import math
import random

def rollDice(amount, max, min = 1):
    sum = 0
    for _ in range(amount):
        sum += random.randint(min, max)
    print (str(amount) + "d" + str(max), "=", str(sum))