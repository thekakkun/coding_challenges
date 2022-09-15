import time
from itertools import permutations

start_time = time.time()


def p068(n):
    """
    Magic 5-gon ring

    Problem 68

    Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

    Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

    It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
    Total	Solution Set
    9	4,2,3; 5,3,1; 6,1,2
    9	4,3,2; 6,2,1; 5,1,3
    10	2,3,5; 4,5,1; 6,1,3
    10	2,5,3; 6,3,1; 4,1,5
    11	1,4,6; 3,6,2; 5,2,4
    11	1,6,4; 5,4,2; 3,2,6
    12	1,5,6; 2,6,4; 3,4,5
    12	1,6,5; 3,5,4; 2,4,6

    By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

    Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
    """

    candidates = [list(x) for x in permutations(range(1, n * 2 + 1))]

    starts_with_smallest = [all([candidate[0] <= x for i, x in enumerate(
        candidate) if i % 2 == 0]) for candidate in candidates]
    candidates = [x for i, x in enumerate(
        candidates) if starts_with_smallest[i]]

    sums = []
    for candidate in candidates:
        line_sums = [[]] * n
        for i in range(n):
            line_sums[i] = candidate[2 * i] + candidate[2 * i + 1]
            line_sums[i] += candidate[2 * i - 1]
        sums.append(line_sums)
    sums_equal = [x.count(x[0]) == n for x in sums]
    candidates = [x for i, x in enumerate(
        candidates) if sums_equal[i]]

    for candidate in candidates:
        for i in range(n):
            candidate.insert((3 * (i + 1)) % (3 * n - 1), candidate[3 * i + 1])
    print(candidates)
    candidates = [''.join([str(x) for x in candidate])
                  for candidate in candidates]

    candidates = [x for x in candidates if len(
        x) == min([len(y) for y in candidates])]

    return max(candidates)


print(p068(3))
print(p068(5))
print('Completed in', time.time() - start_time, 'seconds')
