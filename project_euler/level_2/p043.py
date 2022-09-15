from itertools import permutations
import time

start_time = time.time()


def p043():
    """Sub-string divisibility

    Problem 43

    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

        d_2 d_3 d_4=406 is divisible by 2
        d_3 d_4 d_5=063 is divisible by 3
        d_4 d_5 d_6=635 is divisible by 5
        d_5 d_6 d_7=357 is divisible by 7
        d_6 d_7 d_8=572 is divisible by 11
        d_7 d_8 d_9=728 is divisible by 13
        d_8 d_9 d_10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.
    """

    pandigital_sum = 0

    for pandigital in permutations(range(0, 10)):
        if int(''.join([str(x) for x in pandigital[1:4]])) % 2 != 0:
            continue
        elif int(''.join([str(x) for x in pandigital[2:5]])) % 3 != 0:
            continue
        elif int(''.join([str(x) for x in pandigital[3:6]])) % 5 != 0:
            continue
        elif int(''.join([str(x) for x in pandigital[4:7]])) % 7 != 0:
            continue
        elif int(''.join([str(x) for x in pandigital[5:8]])) % 11 != 0:
            continue
        elif int(''.join([str(x) for x in pandigital[6:9]])) % 13 != 0:
            continue
        elif int(''.join([str(x) for x in pandigital[7:10]])) % 17 != 0:
            continue
        else:
            pandigital_sum += int(''.join([str(x) for x in pandigital]))
    return pandigital_sum


print(p043())
print('Completed in', time.time() - start_time, 'seconds')
