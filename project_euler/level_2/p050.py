import time
from itertools import permutations, combinations, combinations_with_replacement

start_time = time.time()


def p050(prime_under):
    """Problem 50

    The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
    """

    primes_list = list_primes(prime_under / 2)
    term_length = len(primes_list)

    while True:
        print(term_length)
        for i in range(0, len(primes_list) - term_length):
            sum_of_primes = sum(primes_list[i: i + term_length])
            if sum_of_primes > prime_under:
                break
            elif is_prime(sum_of_primes):
                return sum_of_primes

        term_length -= 1

        if term_length == 0:
            break


def list_primes(prime_under):
    primes = [2]
    i = 3
    while i <= prime_under:
        if is_prime(i):
            primes.append(i)
        i += 2

    return primes


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


print(p050(100))
print(p050(1000))
print(p050(1000000))
print('Completed in', time.time() - start_time, 'seconds')
