import time
from functools import reduce

start_time = time.time()


def p047(consecutive_count):
    """Distinct primes factors

    Problem 47

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
    """
    i = 2

    while True:
        prime_check = [is_prime(x)
                       for x in range(i, i + consecutive_count)]
        if any(prime_check):
            i += 1
            continue
        else:
            prime_factors = [factorize(x) for x in range(
                i, i + consecutive_count)]

            overlapping_factors = reduce(lambda x, y: x & y, prime_factors)
            if overlapping_factors:
                i += 1
                continue
            else:
                factor_count_check = [
                    len(x) == consecutive_count for x in prime_factors]
                if not all(factor_count_check):
                    i += 1
                    continue
                else:
                    break
    return i


def factorize(n):
    factors = set()

    # elif n == 1:
    #     return set()
    # else:
    while True:
        if n % 2 == 0:
            factors.add(2)
            n //= 2
        else:
            break

    i = 3

    while i ** 2 <= n:
        if is_prime(i):
            if n % i == 0:
                factors.add(i)
                n //= i
                i = 3
                continue
        i += 2

    if is_prime(n):
        factors.add(n)
    return factors


def is_prime(n):
    if n <= 3:
        return 1 < n
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            else:
                i += 6

    return True


print(p047(2))
print(p047(3))
print(p047(4))
print('Completed in', time.time() - start_time, 'seconds')
