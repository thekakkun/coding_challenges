import time
from math import ceil, sqrt

start_time = time.time()


def p007(n):
    """10001st prime

    Problem 7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10,001st prime number?
    """

    i = 2
    prime_count = 0

    while prime_count != n:
        if is_prime(i):
            prime_count += 1
        i += 1

    return i - 1


def is_prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True


print(p007(6))
print(p007(10001))
print('Completed in', time.time() - start_time, 'seconds')
