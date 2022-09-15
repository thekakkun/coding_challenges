import time

start_time = time.time()


def p033():
    """Digit cancelling fractions

    Problem 33

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
    """

    numerator_product, denominator_product = 1, 1

    for numerator in range(11, 99):
        for denominator in range(numerator + 1, 100):
            divisor = gcd(numerator, denominator)
            if divisor == 1:
                continue
            elif denominator % 10 == 0:
                continue
            else:
                if numerator % 10 == denominator // 10:
                    if (numerator // 10) / (denominator % 10) == numerator / denominator:
                        print(f'{numerator} / {denominator}')
                        numerator_product *= numerator
                        denominator_product *= denominator

    return denominator_product // (gcd(numerator_product, denominator_product))


def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


print(p033())
print('Completed in', time.time() - start_time, 'seconds')
