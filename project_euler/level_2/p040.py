import time
from functools import reduce

start_time = time.time()


def p040(digit_list):
    """Champernowne's constant

    Problem 40

    An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If d_n represents the nth digit of the fractional part, find the value of the following expression.

    d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
    """

    chapernowne_digits = [chapernowne(x) for x in digit_list]
    print(chapernowne_digits)

    return reduce(lambda x, y: x * y, chapernowne_digits)


def chapernowne(n):
    order = 1
    i = n - 1
    while True:
        i -= (10 ** order - 10 ** (order - 1)) * order

        if i < 0:
            break
        else:
            order += 1

    j = order
    place_in_order = n
    while 0 < j:
        j -= 1
        place_in_order -= int((10 ** j - 10 ** (j - 1)) * j)

    digit_from = 10 ** (order - 1) + (place_in_order - 1) // order
    digit = (place_in_order - 1) % order

    return int(str(digit_from)[digit])


print(p040([1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]))
print('Completed in', time.time() - start_time, 'seconds')
