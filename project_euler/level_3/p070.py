import time
from functools import reduce
from itertools import combinations
from math import gcd, sqrt

start_time = time.time()


def p070(max_n):
    """
    Totient permutation

    Problem 70

    Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
    The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

    Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

    Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
    """

    n_over_phi = max_n
    target = 0

    primes_list = list_primes(max_n // 2)

    for i in range(len(primes_list)):
        for j in range(i + 1, len(primes_list)):
            n = primes_list[i] * primes_list[j]
            if n > max_n:
                break
            else:
                phi_n = phi([primes_list[i], primes_list[j]])
                if is_permutation(n, phi_n):
                    if n_over_phi > n / phi_n:
                        n_over_phi = n / phi_n
                        target = n
                        print(n, phi_n, n_over_phi)

    return target
    # for n in range(3, max_n, 2):
    #     if not is_prime(n):
    #         phi_n = phi(n)
    #         if is_permutation(n, phi_n):
    #             if n_over_phi > n / phi_n:
    #                 n_over_phi = n / phi_n
    #                 target = n
    #                 print(n, phi_n, n_over_phi)
    # return target


def phi(factor_list):
    return round(
        reduce(lambda x, y: x * y, factor_list) *
        reduce(lambda x, y: x * (1 - 1/y), factor_list, 1)
    )


def list_primes(primes_under):
    candidates = range(2, primes_under)
    is_prime = [True] * (primes_under - 2)
    for i in range(2, primes_under // 2):
        j = 2
        while i * j - 2 <= primes_under - 3:
            is_prime[i * j - 2] = False
            j += 1

    return [x for i, x in enumerate(candidates) if is_prime[i]]

# def phi(n):
#     factors = prime_factors(n)

#     return int(n * reduce(lambda x, y: x * (1 - 1/y), factors, 1))


# def prime_factors(n):
#     factor_list = set()

#     while n % 2 == 0:
#         n /= 2
#         factor_list.add(2)

#     i = 3
#     while n != 1:
#         while n % i == 0:
#             n /= i
#             factor_list.add(i)
#         i += 2
#     return factor_list


def is_permutation(a, b):
    if sorted(str(a)) == sorted(str(b)):
        return True
    else:
        return False


# def is_prime(n):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True
#     elif n % 2 == 0:
#         return False
#     elif n % 3 == 0:
#         return False
#     else:
#         i = 5

#         while i ** 2 <= n:
#             if n % i == 0:
#                 return False
#             else:
#                 i += 2
#                 continue

#     return True

print(p070(10 ** 7))
print('Completed in', time.time() - start_time, 'seconds')
