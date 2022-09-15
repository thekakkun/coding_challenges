import time
import os

start_time = time.time()


def p056():
    """Powerful digit sum

    Problem 56

    A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

    Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
    """

    max_sum = 0

    for i in range(1, 100):
        for j in range(1, 100):
            digital_sum = sum([int(x) for x in str(i ** j)])
            if max_sum < digital_sum:
                max_sum = digital_sum

    return max_sum


print(p056())
print('Completed in', time.time() - start_time, 'seconds')
