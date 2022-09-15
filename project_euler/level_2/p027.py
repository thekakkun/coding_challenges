import time

start_time = time.time()


def p027():
    """Quadratic primes

    Problem 27

    Euler discovered the remarkable quadratic formula:

    n^2+n+41

    It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

    The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n2+an+b

    , where |a|<1000 and |b|≤1000 where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
    """

    ab_range = 1000

    max_consecutive_primes = 0
    ab_product = 0

    for a in range(-ab_range + 1, ab_range):
        for b in range(-ab_range, ab_range + 1):
            if gcd(a + 1, b) != 1:
                continue
            else:
                n = 0
                while is_prime(n ** 2 + a * n + b):
                    n += 1
                if max_consecutive_primes < n:
                    max_consecutive_primes = n
                    ab_product = a * b
                    print(
                        f'{max_consecutive_primes} consecutive primes when a, b = {a}, {b}')

    return ab_product


def is_prime(n):
    n = abs(n)
    if n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    i = 3
    while i ** 2 < n:
        if n % i == 0:
            return False
        i += 2

    return True


def gcd(a, b):
    if b < a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


print(p027())
print('Completed in', time.time() - start_time, 'seconds')
