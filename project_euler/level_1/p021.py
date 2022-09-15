import time

start_time = time.time()


def p021(n):
    """Amicable numbers

    Problem 21

    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """

    amicable_numbers = []

    for i in range(1, n + 1):
        if i in amicable_numbers:
            i += 1
            continue
        else:
            sum_of_divisors = divisor_sum(i)
            if i == divisor_sum(sum_of_divisors) and i != sum_of_divisors:
                amicable_numbers.extend((i, sum_of_divisors))
        i += 1

    return sum(amicable_numbers)


def divisor_sum(n):
    divisor_list = [1]
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            divisor_list.extend((i, n // i))
        i += 1

    return sum(divisor_list)


print(p021(10000))
print('Completed in', time.time() - start_time, 'seconds')
