import time
from itertools import combinations, combinations_with_replacement, permutations

start_time = time.time()


def p049():
    """Prime permutations

    Problem 49

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this sequence?
    """

    for i in combinations_with_replacement(range(0, 10), 4):
        permutation_list = [int(''.join([str(x) for x in y]))
                            for y in permutations(i)]
        prime_numbers = set([
            x for x in permutation_list if is_prime(x) and len(str(x)) == 4])

        if len(prime_numbers) < 3:
            continue
        else:
            for j in combinations(prime_numbers, 2):
                gap = j[1] - j[0]
                if j[1] + gap in prime_numbers:
                    print(f'{j[0]}{j[1]}{j[1] + gap}')


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
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
                continue

    return True


print(p049())
print('Completed in', time.time() - start_time, 'seconds')
