import time
from functools import reduce
from math import ceil, sqrt

start_time = time.time()


def p005(n):
    """Smallest multiple

    Problem 5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    prod = 1

    for i in range(2, n + 1):
        divisor = gcd(prod, i)
        prod = prod * i // divisor

    return prod


def gcd(a, b):
    if b > a:
        temp = a
        a = b
        b = temp

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a


print(p005(10))
print(p005(20))
print('Completed in', time.time() - start_time, 'seconds')
