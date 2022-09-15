import time
from copy import deepcopy
from math import sqrt

start_time = time.time()


def p066(max_d):
    """
    Diophantine equation

    Problem 66

    Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

    For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

    It can be assumed that there are no solutions in positive integers when D is square.

    By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

    Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

    Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
    """

    max_x = 0
    target_d = 0

    for d in range(2, max_d + 1):

        if sqrt(d) % 1 == 0:
            continue

        sequence = [int(sqrt(d)), []]
        num, den = 1, sequence[0]

        while True:
            sequence[1].append(int((sqrt(d) + den) / ((d - den ** 2) / num)))
            num = (d - den ** 2) / num
            den = num * sequence[1][-1] - den

            x, y = get_expansion(deepcopy(sequence))
            if x ** 2 - d * y ** 2 == 1:
                print(f'{x}^2 - {d}*{y}^2 = 1')
                if max_x < x:
                    max_x = x
                    target_d = d
                break

    return target_d


def get_expansion(sequence):
    if sequence[1]:
        num, den = 1, sequence[1].pop()

    while sequence[1]:
        num, den = den, den * sequence[1].pop() + num

    return (num + sequence[0] * den, den)


print(p066(7))
print(p066(1000))
print('Completed in', time.time() - start_time, 'seconds')
