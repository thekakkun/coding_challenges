import time

start_time = time.time()


def p052():
    """Permuted multiples

    Problem 52

    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """

    i = 1
    while True:
        for j in range(6, 1, -1):
            if not has_same_digits(i, i * j):
                i += 1
                break
        else:
            return i


def has_same_digits(a, b):
    a_list, b_list = [int(x) for x in str(a)], [int(x) for x in str(b)]
    if len(str(a_list)) != len(str(b_list)):
        return False
    else:
        for i in range(0, 10):
            if a_list.count(i) != b_list.count(i):
                return False
        else:
            return True


print(p052())
print('Completed in', time.time() - start_time, 'seconds')
