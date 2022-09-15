import time

start_time = time.time()


def p032():
    """Pandigital products

    Problem 32

    We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
    """

    pandigital_products = []

    for i in range(2, 100):
        for j in range(100, 10000):
            if ''.join(sorted(str(i) + str(j) + str(i * j))) == '123456789':
                print(f'{i} * {j} = {i * j}')

                if i * j not in pandigital_products:
                    pandigital_products.append(i * j)

    return sum(pandigital_products)


# def product_is_pandigital(a, b):
#     first_digit_a, first_digit_b = str(a)[-1], str(b)[-1]
#     if first_digit_a == '1' or first_digit_b == '1':
#         return False

#     number_list = [x for x in str(a) + str(b) + str(a * b)]

#     if '0' in number_list:
#         return False
#     elif len(number_list) != 9:
#         return False
#     elif len(set(number_list)) != 9:
#         return False
#     else:
#         return True

#     product = str(a * b)
#     number_list = [x for x in str(a) + str(b) + str(product)]

#     invalid_multiplications = {
#         0: [1, 2, 3, 4, 5, 6, 7, 8, 9],
#         1: [1],
#         2: [1, 6],
#         3: [1],
#         4: [1, 6],
#         5: [1, 3, 5, 7, 9],
#         6: [1, 6],
#         7: [1],
#         8: [1, 6],
#         9: [1]
#     }

#     if first_digit_a in invalid_multiplications[first_digit_b]:
#         return False
#     if '0' in number_list:
#         return False
#     elif len(str(a)) + len(str(b)) + len(str(product)) != 9:
#         return False
#     elif len(set(number_list)) == 9:
#         return True
#     else:
#         return False


print(p032())
print('Completed in', time.time() - start_time, 'seconds')
