import time

start_time = time.time()


def p039():
    """Integer right triangles

    Problem 39

    If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    """

    pythagorean_triplets = []

    m, n = 2, 1

    while True:
        if m <= n:
            m += 1
            n = 1
            continue
        elif 500 < m * (m + n):
            break
        elif (m + n) % 2 != 1:
            n += 1
            continue
        elif is_coprime(m, n):
            pythagorean_triplets.append(
                [m ** 2 - n ** 2, 2 * m * n, m ** 2 + n ** 2]
            )
        n += 1
        continue

    perimeter_list = [sum(x) for x in pythagorean_triplets]
    max_solution_count = 0
    max_solution_perimiter = 0

    for i in range(min(perimeter_list), max(perimeter_list)):
        solution_count = len(
            [x for x in perimeter_list if x <= i and i % x == 0])
        if max_solution_count < solution_count:
            max_solution_count = solution_count
            max_solution_perimiter = i

    return max_solution_perimiter


def is_coprime(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    if a == 1:
        return True
    else:
        return False


print(p039())
print('Completed in', time.time() - start_time, 'seconds')
