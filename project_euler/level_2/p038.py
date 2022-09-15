import time

start_time = time.time()


def p038():
    """Pandigital multiples

    Problem 38

    Take the number 192 and multiply it by each of 1, 2, and 3:

        192 × 1 = 192
        192 × 2 = 384
        192 × 3 = 576

    By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
    """

    max_pandigital_multiple = 0

    for i in range(1, 100000):
        digits = []
        n = 1

        while True:
            product_digits = [int(x) for x in str(i * n)]
            if 0 in product_digits:
                break
            elif any([x in digits for x in product_digits]):
                break
            else:
                digits.extend(product_digits)

                if len(digits) < 9:
                    n += 1
                    continue
                elif len(digits) == 9:
                    if sorted(digits) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        pandigital_multiple = int(''.join(map(str, digits)))
                        if max_pandigital_multiple < pandigital_multiple:
                            max_pandigital_multiple = pandigital_multiple
                    break
                else:
                    break

            digits.extend([int(x) for x in str(i * n)])

    return max_pandigital_multiple


print(p038())
print('Completed in', time.time() - start_time, 'seconds')
