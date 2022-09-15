import time
from math import gcd
from itertools import combinations
from functools import reduce

start_time = time.time()


def p069(max_n):
    """
    Totient maximum

    Problem 69

    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
    n   Relatively Prime    φ(n)    n/φ(n)
    2   1                   1       2
    3   1,2                 2       1.5
    4   1,3                 2       2
    5   1,2,3,4             4       1.25
    6   1,5                 2       3
    7   1,2,3,4,5,6         6       1.1666...
    8   1,3,5,7             4       2
    9   1,2,4,5,7,8         6       1.5
    10 	1,3,7,9             4       2.5

    It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

    Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
    """

    n_over_phi = 0
    target = 0

    for n in range(2, max_n + 1):
        phi_n = phi(n)
        if n_over_phi < n / phi_n:
            n_over_phi = n / phi_n
            target = n
            print(n)

    return target


def phi(n):
    factors = prime_factors(n)

    return int(n * reduce(lambda x, y: x * (1 - 1/y), factors, 1))

    # phi = n
    # factors = prime_factors(n)
    # for i in factors:
    #     phi -= n // i
    # if len(factors) >= 2:
    #     for i in range(2, len(factors)):
    #         for factor_combination in combinations(factors, i):
    #             phi += (n - 1) // (reduce(lambda x,
    #                                       y: x * y, factor_combination))

    # return phi + len(factors) - 1


def prime_factors(n):
    factor_list = set()

    while n % 2 == 0:
        n /= 2
        factor_list.add(2)

    i = 3
    while n != 1:
        while n % i == 0:
            n /= i
            factor_list.add(i)
        i += 2
    return factor_list


print(p069(10))
print(p069(1000000))
print('Completed in', time.time() - start_time, 'seconds')
