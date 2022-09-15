import time

start_time = time.time()


def p028(n):
    """Number spiral diagonals

    Problem 28

    Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
    """

    diagonal_sum = 1
    ring = 2

    while True:
        # diagonal_sum += 4 * ((2 * ring - 3) ** 2) + (ring - 1) * 20
        diagonal_sum += 4 * (4 * ring ** 2 - 7 * ring + 4)

        if ring * 2 - 1 == n:
            break

        ring += 1

    return diagonal_sum


print(p028(5))
print(p028(1001))
print('Completed in', time.time() - start_time, 'seconds')
