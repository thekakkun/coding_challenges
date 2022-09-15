import time

start_time = time.time()


def p004(digits):
    """Largest palindrome product

    Problem 4

    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    prod = 0
    factors = range(10 ** digits - 1, 1, -1)

    for i in factors:
        for j in factors:
            n = i * j
            if str(n) == str(n)[::-1]:
                if prod < n:
                    prod = n

    return prod


print(p004(2))
print(p004(3))
print('Completed in', time.time() - start_time, 'seconds')
