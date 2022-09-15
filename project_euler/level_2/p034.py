import time
from functools import reduce

start_time = time.time()


def p034():
    """Digit factorials

    Problem 34

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    NOTE: as 1! = 1 and 2! = 2 are not sums they are not included.
    """

    digit_factorial_sum = 0

    for i in range(3, 7 * factorial(9)):
        if i == reduce(lambda x, y: int(x) + factorial(int(y)), str(i), 0):
            print(i)
            digit_factorial_sum += i

    return digit_factorial_sum


def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))


print(p034())
print('Completed in', time.time() - start_time, 'seconds')
