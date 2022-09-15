import time

start_time = time.time()


def p006(n):
    """Sum square difference

    Problem 6

    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """

    sum_square_difference = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                sum_square_difference += i * j

    return sum_square_difference


print(p006(10))
print(p006(100))
print('Completed in', time.time() - start_time, 'seconds')
