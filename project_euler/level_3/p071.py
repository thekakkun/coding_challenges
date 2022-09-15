import time
from math import gcd

start_time = time.time()


def p071(target, max_d):
    """
    Ordered fractions

    Problem 71

    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that 2/5 is the fraction immediately to the left of 3/7.

    By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
    """

    solution = 0
    min_diff = max_d

    for d in range(2, max_d + 1):
        if d % target[1] == 0:
            continue
        closest_n = int(d * target[0] / target[1])
        if gcd(closest_n, d) != 1:
            continue
        if target[0] / target[1] - closest_n / d < min_diff:
            min_diff = target[0] / target[1] - closest_n / d
            solution = closest_n

    return solution


print(p071([3, 7], 1000000))
print('Completed in', time.time() - start_time, 'seconds')
