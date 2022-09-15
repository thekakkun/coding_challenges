import time
from math import ceil, sqrt

start_time = time.time()


def p003(n):
    """Largest prime factor

    Problem 3

    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """

    factors = []

    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            factors.append(i)
            n /= i

    return max(factors)


print(p003(13195))
print(p003(600851475143))
print('Completed in', time.time() - start_time, 'seconds')
