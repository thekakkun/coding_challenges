import csv
import os
import time

start_time = time.time()


def p067(triangle):
    """
    By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
    """

    while len(triangle) != 1:
        for i in range(len(triangle[-2])):
            triangle[-2][i] = max(
                triangle[-2][i] + triangle[-1][i],
                triangle[-2][i] + triangle[-1][i + 1]
            )
        triangle.pop()

    return triangle[0][0]


with open(os.path.join('level_3', 'p067_triangle.txt'), 'r') as f:
    triangle = csv.reader(f, delimiter=' ')
    triangle = [[int(x) for x in row] for row in triangle]
    print(p067(triangle))
print('Completed in', time.time() - start_time, 'seconds')
