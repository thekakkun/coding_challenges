import time
from functools import reduce

start_time = time.time()


def p024(digits, n):
    """Lexicographic permutations

    Problem 24

    A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """

    digit_list = list(range(digits))
    nth_value = ''

    while True:
        element = (n - 1) // factorial(len(digit_list) - 1)
        nth_value += str(digit_list.pop(element))

        if len(digit_list) == 1:
            nth_value += str(digit_list[0])
            break

        n = (n) % factorial(len(digit_list))

    return nth_value


def factorial(n):
    return reduce(lambda x, y: x * y, list(range(1, n + 1)))


print(p024(10, 1000000))
print('Completed in', time.time() - start_time, 'seconds')
