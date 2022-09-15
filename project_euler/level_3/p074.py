import time
from functools import reduce
from itertools import combinations_with_replacement, permutations


start_time = time.time()


def p074(max_n, target):
    """
    Digit factorial chains

    Problem 74

    The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

    Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872

    It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

    69 → 363600 → 1454 → 169 → 363601 (→ 1454)
    78 → 45360 → 871 → 45361 (→ 871)
    540 → 145 (→ 145)

    Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

    How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
    """
    matches = set()

    r = 1
    while True:
        candidates = combinations_with_replacement(range(10), r)

        for candidate in candidates:
            n = int(''.join([str(x) for x in candidate]))
            n *= 10 ** (candidate.count(0))

            if int(''.join([str(x) for x in candidate])) > max_n:
                return len(matches)

            if len(get_chain(n)) == target:
                for foo in permutations(candidate):
                    n = int(''.join([str(x) for x in foo]))

                    if n < max_n:
                        if len(get_chain(n)) == target:
                            matches.add(n)

        r += 1

    # count = 0
    # loop_lengths = {}

    # for i in range(1, max_n + 1):
    #     loop = []

    #     while True:
    #         if i in loop_lengths:
    #             length = len(loop) + loop_lengths[i]
    #             break

    #         if i in loop:
    #             for j, x in enumerate(loop):
    #                 loop_lengths[x] = len(loop) - min(j, loop.index(i))
    #             length = len(loop)
    #             break

    #         loop.append(i)
    #         i = digit_factorial(i)

    #     if length == target:
    #         print(loop[0])
    #         count += 1


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(2, n + 1))


def digit_factorial(n):
    factorial_sum = 0
    while 1 <= n:
        factorial_sum += factorial(n % 10)
        n //= 10

    return factorial_sum


def get_chain(n, history=None):
    if history is None:
        history = []

    if n in history:
        return history
    else:
        history.append(n)
        return get_chain(digit_factorial(n), history)


print(p074(1000000, 60))
print('Completed in', time.time() - start_time, 'seconds')
