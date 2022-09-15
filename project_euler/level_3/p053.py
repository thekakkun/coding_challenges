import time
from math import comb

start_time = time.time()


def p053():
    """Combinatoric selections

    Problem 53

    There are exactly ten ways of selecting three from five, 12345:

        123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

    In combinatorics, we use the notation, (5,3)=10.
    
    In general, (n,r)=n! / r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

    It is not until n=23, that a value exceeds one-million: (23,10)=1144066.
    How many, not necessarily distinct, values of (n,r) for 1≤n≤100, are greater than one-million?
    """

    count = 0

    for n in range(1, 101):
        if n == 23:
            print('hey')
        for r in range(n, 0, -1):
            if comb(n, r) > 1_000_000:
                count += 1

    return count



print(p053())
print('Completed in', time.time() - start_time, 'seconds')
