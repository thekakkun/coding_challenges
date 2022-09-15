import time
from functools import reduce

start_time = time.time()


def p020(n):
    """Factorial digit sum

    Problem 20

    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """

    return reduce(lambda x, y: int(x) + int(y), str(factorial(n)))


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(p020(10))
print(p020(100))
print('Completed in', time.time() - start_time, 'seconds')
