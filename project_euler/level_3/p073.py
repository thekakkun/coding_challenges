import time
from math import gcd

start_time = time.time()


def p073(max_d, frac_between):
    """
    Counting fractions in a range

    Problem 73

    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that there are 3 fractions between 1/3 and 1/2.

    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
    """

    frac_count = 0
    primes = list_primes(max_d)

    for i in range(2, max_d + 1):
        candidates = [x for x in range(1, i + 1) if (frac_between[0]
                                                     < x/i < frac_between[1])]
        candidates = [x for x in candidates if gcd(i, x) == 1]

        frac_count += len(candidates)

    return frac_count


def list_primes(max_p):
    is_prime = [True] * (max_p - 1)

    for i in range(max_p - 1):
        if is_prime[i]:
            j = 1
            while i + j * (i + 2) < max_p - 1:
                is_prime[i + j * (i + 2)] = False
                j += 1

    return [1] + [x for i, x in enumerate(range(2, max_p + 1)) if is_prime[i]]


print(p073(8, [1/3, 1/2]))
print(p073(12000, [1/3, 1/2]))
print('Completed in', time.time() - start_time, 'seconds')
