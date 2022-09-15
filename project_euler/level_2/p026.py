import time

start_time = time.time()


def p026(n):
    """Reciprocal cycles

    Problem 26

    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

        1/2	= 	0.5
        1/3	= 	0.(3)
        1/4	= 	0.25
        1/5	= 	0.2
        1/6	= 	0.1(6)
        1/7	= 	0.(142857)
        1/8	= 	0.125
        1/9	= 	0.(1)
        1/10	= 	0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    """

    repeat_digit = []

    for i in range(1, n):
        current_divisor = i
        if i == 1:
            repeat_digit.append(1)
            continue
        else:
            while i % 2 == 0:
                i //= 2
            while i % 5 == 0:
                i //= 5
            if i != current_divisor:
                repeat_digit.append(repeat_digit[i-1])
                continue
            else:
                repeat_count = 1
                while True:
                    if (10 ** repeat_count - 1) % i == 0:
                        repeat_digit.append(repeat_count)
                        break
                    repeat_count += 1

    return repeat_digit.index(max(repeat_digit)) + 1


print(p026(1000))
print('Completed in', time.time() - start_time, 'seconds')
