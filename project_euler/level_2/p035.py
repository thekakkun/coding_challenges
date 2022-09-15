import time

start_time = time.time()


def p035(n):
    """Circular primes

    Problem 35

    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
    """

    circular_primes = []

    for i in range(2, n):
        if i in circular_primes:
            continue
        if is_prime(i):
            if len(str(i)) == 1:
                circular_primes.append(i)
            else:
                possible_primes = []
                digit_list = list(str(i))
                for _ in range(len(digit_list)):
                    digit_list.append(digit_list.pop(0))
                    next_rotation = int(''.join(digit_list))
                    if is_prime(next_rotation):
                        if next_rotation in possible_primes:
                            continue
                        possible_primes.append(next_rotation)
                    else:
                        break
                else:
                    circular_primes.extend(possible_primes)

    print(circular_primes)
    return len(circular_primes)


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3

        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 1

    return True


print(p035(100))
print(p035(1000000))
print('Completed in', time.time() - start_time, 'seconds')
