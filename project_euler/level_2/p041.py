import time
from itertools import permutations

start_time = time.time()


def p041():
    """Pandigital prime

    Problem 41

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """

    for i in range(9, 1, -1):
        pandigital_list = [int(''.join([str(x) for x in y]))
                           for y in permutations(range(1, i + 1))]
        pandigital_list.sort(reverse=True)

        for num in pandigital_list:
            if is_prime(num):
                return num


def is_prime(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        i = 5
        while i ** 2 <= n:
            if n % i == 0:
                return False
            else:
                i += 2
    return True


print(p041())
print('Completed in', time.time() - start_time, 'seconds')
