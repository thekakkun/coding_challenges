import time
from functools import reduce

start_time = time.time()


def p016(power):
    """Power digit sum

    Problem 16

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """

    product = 2 ** power

    return reduce(lambda x, y: x + int(y), str(product), 0)


print(p016(15))
print(p016(1000))
print('Completed in', time.time() - start_time, 'seconds')
