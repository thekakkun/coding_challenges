import time
from random import randint

start_time = time.time()


def p060(n):
    """Prime pair sets

    Problem 60

    The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

    Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
    """

    valid_chains = []

    prime_list = [3]

    while True:
        next_prime = get_next_prime(prime_list[-1])
        invalid_primes = []
        valid_chains.sort(key=lambda x: (-len(x), x))

        for chain in valid_chains:
            if bool(set(invalid_primes) & set(chain)):
                continue
            for prime in chain:
                prime_pair = [prime, next_prime]
                if not concatenate_prime_check(*prime_pair):
                    invalid_primes.append(prime)
                    break
            else:
                new_chain = chain + [next_prime]
                if len(new_chain) == n:
                    print(new_chain)
                    return sum(new_chain)
                else:
                    valid_chains.append(new_chain)

        for prime in prime_list:
            if prime in invalid_primes:
                continue
            prime_pair = [prime, next_prime]
            if concatenate_prime_check(*prime_pair):
                if prime_pair not in valid_chains:
                    valid_chains.append(prime_pair)

        prime_list.append(next_prime)


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

# def is_prime(n, k=3):
#     if n <= 1:
#         return False
#     elif n <= 3:
#         return True

#     for _ in range(k):
#         a = randint(2, n - 2)
#         if (a ** (n - 1)) % n != 1:
#             return False

#     return True

def is_prime(n, k=8):
    r = 0
    d = n - 1

    while d % 2 == 0:
        d = int(d / 2)
        r += 1

    for i in range(k):
        a = randint(2, n - 2)

        x = (a ** d) % n
        if x == 1 or x == (n - 1):
            continue
        for j in range(r - 1):
            x = (x ** 2) % n
            if x == (n - 1):
                continue
        return False
    return True


def get_next_prime(n):
    n += 2
    while True:
        if is_prime(n):
            return n
        n += 2


def concatenate_prime_check(a, b):
    if is_prime(int(''.join(str(a) + str(b)))):
        if is_prime(int(''.join(str(b) + str(a)))):
            return True
    return False


print(p060(4))
# print(p060(5))
print('Completed in', time.time() - start_time, 'seconds')
