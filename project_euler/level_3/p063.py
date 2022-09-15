import time

start_time = time.time()


def p063():
    """Powerful digit counts

    Problem 63

    The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?
    """

    count = 0
    base, power = 1, 1

    while True:
        if len(str(base ** power)) == power:
            count += 1
            print(f'{count}: {base}^{power} = {base ** power}')
        if base == 9:
            if len(str(base ** power)) == power:
                power += 1
                base = 1
                continue
            else:
                return count
        base += 1


print(p063())
print('Completed in', time.time() - start_time, 'seconds')
