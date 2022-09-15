import time

start_time = time.time()


def p046():
    """Goldbach's other conjecture

    Problem 46

    It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
    """

    i = 9

    while True:
        if is_prime(i):
            i += 2
            continue
        else:
            j = 1
            while 2 * (j ** 2) < i:
                if is_prime(i - 2 * (j ** 2)):
                    print(f'{i} = {i - 2 * (j ** 2)} + 2 * {j}^2')
                    i += 2
                    break
                else:
                    j += 1
                    continue
            else:
                return i


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n == 3:
        return True
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


print(p046())
print('Completed in', time.time() - start_time, 'seconds')
