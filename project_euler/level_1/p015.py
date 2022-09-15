import time
from functools import reduce

start_time = time.time()


def p014(lattice_size):
    """Lattice paths

    Problem 15

    Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """

    return factorial(lattice_size[0] + lattice_size[1]) // (factorial(lattice_size[0]) * factorial(lattice_size[1]))


def factorial(n):
    """Calculate factorial
    """

    return reduce(lambda x, y: x * y, range(1, n + 1))


print(p014([2, 2]))
print(p014([20, 20]))
print('Completed in', time.time() - start_time, 'seconds')
