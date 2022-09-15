import time

start_time = time.time()


def p036():
    """Double-base palindromes

    Problem 36

    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
    """

    palindromic_sum = 0

    for i in range(1000000):
        if i == int(str(i)[::-1]):
            if int(bin(i)[2:]) == int(bin(i)[-1:1:-1]):
                print(i, bin(i))
                palindromic_sum += i

    return palindromic_sum


print(p036())
print('Completed in', time.time() - start_time, 'seconds')
