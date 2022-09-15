import time
from itertools import permutations

start_time = time.time()


def p051(target_family_size):
    """Prime digit replacements

    Problem 51

    By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
    """

    n = 55003

    while True:
        if not is_prime(n):
            n += 2
            continue
        else:
            digits = [int(x) for x in str(n)]
            for i in range(0, 10):
                family_size = 1
                digit_idx = [j for j, x in enumerate(digits) if x == i]

                if len(digit_idx) >= 2:
                    for replace_count in range(len(digit_idx), 1, -1):
                        for idx_list in permutations(digit_idx, replace_count):
                            family_size = 1
                            for j in range(i + 1, 10):
                                digits_temp = digits.copy()
                                for idx in idx_list:
                                    digits_temp[idx] = j

                                if is_prime(int(''.join([str(x) for x in digits_temp]))):
                                    family_size += 1

                            if family_size == target_family_size:
                                return n
            n += 2


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


print(p051(7))
print(p051(8))
print('Completed in', time.time() - start_time, 'seconds')
