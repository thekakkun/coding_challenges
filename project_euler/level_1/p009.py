import time
from math import ceil

start_time = time.time()


def p009(n):
    """Special Pythagorean triplet

    Problem 9

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    for a in range(1, ceil((n-3)/3)):
        for b in range(a+1, ceil((n-a)/2)):
            c = 1000 - a - b

            if a**2 + b**2 == c**2:
                return a * b * c


print(p009(1000))
print('Completed in', time.time() - start_time, 'seconds')
