import time

start_time = time.time()


def p023(upper_limit=28123):
    """Non-abundant sums

    Problem 23

    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    """

    abundant_list = get_abundant_numbers(upper_limit)
    all_values = set(range(1, upper_limit + 1))
    abundant_sums = set()

    for i, e1 in enumerate(abundant_list):
        for e2 in abundant_list[i:]:
            abundant_sum = e1 + e2
            if upper_limit < abundant_sum:
                break
            else:
                abundant_sums.add(abundant_sum)

    return sum(all_values - abundant_sums)

    # total = 0

    # for i in range(1, upper_limit + 1):
    #     possible_values = [x for x in abundant_list if x < i]

    #     if len(possible_values) <= 1:
    #         total += i
    #         continue
    #     else:
    #         for j in possible_values:
    #             if (i - j) in possible_values:
    #                 break
    #         else:
    #             total += i

    # return total


def get_factors(n):
    factor_list = [1]

    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            if i != n // i:
                factor_list.extend((i, n // i))
            else:
                factor_list.append(i)
        i += 1

    return sorted(factor_list)


def is_abundant(n):
    sum_of_factors = sum(get_factors(n))

    if n < sum_of_factors:
        return True
    else:
        return False


def get_abundant_numbers(n):
    abundant_list = []
    for i in range(1, n + 1):
        if is_abundant(i):
            abundant_list.append(i)

    return abundant_list


print(p023())
print('Completed in', time.time() - start_time, 'seconds')
