import time

start_time = time.time()


def p048(n):
    """Self powers

    Problem 48

    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """

    series_sum = 0

    for i in range(1, n + 1):
        series_sum += i ** i

    return series_sum


print(p048(10))
print(p048(1000))
print('Completed in', time.time() - start_time, 'seconds')
