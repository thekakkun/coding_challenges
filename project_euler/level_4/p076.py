import time
from math import ceil, floor, sqrt

start_time = time.time()


def p076(n):
    """
    Counting summations

    Problem 76

    It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

    How many different ways can one hundred be written as a sum of at least two positive integers?
    """

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        k_range = range(ceil(-(sqrt(24 * n + 1) - 1) / 6),
                        floor((sqrt(24 * n + 1) + 1) / 6) + 1)
        series = [int((-1) ** (k + 1) * p076(int(n - k * (3 * k - 1) / 2)))
                  for k in k_range if k != 0]
        return sum(series)

    # if k is None:
    #     k = 1

    # if k > abs(len(coin_list)) or n < 0 or n < k:
    #     return 0
    # elif n == 0 or n == k:
    #     return 1
    # else:
    #     return p076(coin_list, n, k+1) + \
    #         p076(coin_list, n - coin_list[k - 1], k)


def rule_asc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        print(x, a)
        yield a[:k + 1]


# print(p076(24))
print(list((rule_asc(5))))
print('Completed in', time.time() - start_time, 'seconds')
