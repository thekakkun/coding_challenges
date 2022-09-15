import time

start_time = time.time()


def p072(max_d):
    """
    Counting fractions

    Problem 72

    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that there are 21 elements in this set.

    How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
    """

    phi_list = list(range(2, max_d + 1))
    is_prime = [True] * (max_d - 1)

    for i in range(max_d - 1):
        if is_prime[i]:
            j = 1
            while j * (i + 2) - 2 < max_d - 1:
                if j != 1:
                    is_prime[j * (i + 2) - 2] = False
                phi_list[j * (i + 2) - 2] *= 1 - 1 / (i + 2)
                j += 1

    phi_list = [round(x) for x in phi_list]

    return sum(phi_list)


#     elements = 0

#     for i in range(2, max_d + 1):
#         elements += phi(i)

#     return elements


# def phi(n):
#     prime_factors = [x for x in prime_list(n) if n % x == 0]

#     return round(reduce(lambda x, y: x * (1 - 1/y), prime_factors, n))


# def prime_list(max_p):
#     p_list = range(2, max_p + 1)
#     is_prime = [True] * (max_p - 1)

#     for i in range(0, max_p - 1):
#         if p_list[i] > sqrt(max_p):
#             break
#         if is_prime[i]:
#             j = 1
#             while True:
#                 if i + p_list[i] * j >= max_p - 1:
#                     break
#                 is_prime[i + p_list[i] * j] = False
#                 j += 1
#     return [p_list[i] for i, x in enumerate(is_prime) if x]


print(p072(8))
print(p072(12000))
print(p072(1000000))
print('Completed in', time.time() - start_time, 'seconds')
