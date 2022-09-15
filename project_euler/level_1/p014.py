import time

start_time = time.time()


def p014(n):
    """Longest Collatz sequence

    Problem 14

    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

    collatz_accumulator = {}

    for i in range(1, n):
        step = 1
        current_number = i

        while True:
            if current_number in collatz_accumulator:
                step += collatz_accumulator[current_number] - 1
                collatz_accumulator[i] = step
                break

            if i == 1:
                collatz_accumulator[i] = step
                break
            elif current_number % 2 == 0:
                current_number = current_number // 2
                step += 1
            else:
                current_number = 3 * current_number + 1
                step += 1

    return max(collatz_accumulator.keys(),
               key=lambda x: collatz_accumulator[x])


print(p014(1000000))
print('Completed in', time.time() - start_time, 'seconds')
