import time

start_time = time.time()


def p031(n, coin_types):
    """Coin sums

    Problem 31

    In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

    How many different ways can £2 be made using any number of coins?
    """

    if n == 0:
        return 1
    else:
        coin_types = [x for x in coin_types if x <= n]

        if n < 0 or len(coin_types) == 0:
            return 0
        else:
            return p031(n, coin_types[:-1]) + \
                p031(n - coin_types[-1], coin_types)


coin_types = [1, 2, 5, 10, 20, 50, 100, 200]

print(p031(5, coin_types))
print(p031(200, coin_types))
print('Completed in', time.time() - start_time, 'seconds')
