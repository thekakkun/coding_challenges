import time

start_time = time.time()


def p062(count):
    """Cubic permutations

    Problem 62

    The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits are cube.
    """

    cubes = []

    while True:
        cubes.append((len(cubes) + 1) ** 3)

        if len([x for x in cubes if is_permutation(x, cubes[-1])]) == count:
            return min([x for x in cubes if is_permutation(x, cubes[-1])])
        else:
            continue


def is_permutation(a, b):
    if len(str(a)) != len(str(b)):
        return False
    elif sorted([int(x) for x in str(a)]) == sorted([int(x) for x in str(b)]):
        return True
    else:
        return False


print(p062(3))
print(p062(5))
print('Completed in', time.time() - start_time, 'seconds')
