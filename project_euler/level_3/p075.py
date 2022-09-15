import time
from math import gcd

start_time = time.time()


def p075(max_l):
    """
    Singular integer right triangles

    Problem 75

    It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

    In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

    Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
    """

    wire_lengths = []

    n = 1
    m = n + 1
    l = 2 * m**2 + 2 * m * n

    while l <= max_l:
        while l <= max_l:
            k = 1
            while l <= max_l:
                wire_lengths.append(l)
                k += 1
                l = k * (2 * m**2 + 2 * m * n)

            while True:
                m += 2
                if gcd(m, n) == 1:
                    break
            l = 2 * m**2 + 2 * m * n

        n += 1
        m = n + 1
        l = 2 * m**2 + 2 * m * n

    len_count = {}
    for l in wire_lengths:
        len_count[l] = len_count.get(l, 0) + 1

    return len([k for k, v in len_count.items() if v == 1])


print(p075(1500000))
print('Completed in', time.time() - start_time, 'seconds')
