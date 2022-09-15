import time

start_time = time.time()


def p037():
    """Truncatable primes

    Problem 37

    The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    """

    truncatable_primes = []
    i = 11

    while len(truncatable_primes) < 11:
        if not is_prime(i):
            i += 2
            continue
        for j in range(1, len(str(i))):
            if is_prime(int(str(i)[:-j])) and is_prime(int(str(i)[j:])):
                continue
            else:
                i += 2
                break
        else:
            truncatable_primes.append(i)
            print(i)
            i += 2

    return sum(truncatable_primes)


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    else:
        i = 3

        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 2
        return True

print(p037())
print('Completed in', time.time() - start_time, 'seconds')
