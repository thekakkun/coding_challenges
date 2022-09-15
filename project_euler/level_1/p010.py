import time

start_time = time.time()


def p010(n):
    """Summation of primes

    Problem 10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """

    i = 2
    sum_of_primes = 0

    while i < n:
        if is_prime(i):
            sum_of_primes += i
        i += 1

    return sum_of_primes


def is_prime(n):
    """check if prime
    """

    if n <= 3:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False

    i = 5
    while i**2 <= n:
        if n % i == 0:
            return False
        else:
            i += 2

    return True


print(p010(10))
print(p010(2e6))
print('Completed in', time.time() - start_time, 'seconds')
