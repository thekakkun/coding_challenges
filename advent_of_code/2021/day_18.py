# https://adventofcode.com/2021/day/18

from functools import reduce
from math import ceil, floor


def parse_input(text):
    text = text.strip()
    assignment = []

    for line in text.splitlines():
        num = []
        e = ''
        for c in line:
            if c.isspace():
                continue
            elif c.isdecimal():
                e += c
            else:
                if e:
                    num.append(int(e))
                    e = ''
                num.append(c)
        assignment.append(num)

    return assignment


def is_explodable(num, depth=0):
    depth = 0
    for i, c in enumerate(num):
        if c == '[':
            depth += 1
            if depth == 5:
                return (True,  i + 1)
        elif c == ']':
            depth -= 1

    return (False, -1)


def explode(num):
    explodable, loc = is_explodable(num)
    if not explodable:
        return num

    e1, e2 = num[loc], num[loc + 2]
    num[loc - 1: loc + 4] = [0]

    for i, e in enumerate(num[loc-2::-1]):
        if isinstance(e, int):
            num[loc-i-2] = e + e1
            break
    for i, e in enumerate(num[loc+1:], loc+1):
        if isinstance(e, int):
            num[i] = e + e2
            break

    return num


def is_splittable(num):
    digits = 0
    for i, c in enumerate(num):
        if isinstance(c, int):
            if 9 < c:
                return (True, i)
        else:
            digits = 0

    return (False, -1)


def split(num):
    splittable, loc = is_splittable(num)
    if not splittable:
        return num

    (e1, e2) = floor(num[loc]/2), ceil(num[loc]/2)
    num[loc:loc+1] = ['[', e1, ',', e2, ']', ]

    return num


def add(num_1, num_2):
    num = []
    num.append('[')
    num += num_1
    num.append(',')
    num += num_2
    num.append(']')

    while True:
        if is_explodable(num)[0]:
            num = explode(num)
        elif is_splittable(num)[0]:
            num = split(num)
        else:
            break

    return num


def get_magnitude(num):
    magnitude = 0

    if isinstance(num[0], str):
        num = eval(to_string(num))

    for i, e in enumerate(num):
        if isinstance(e, int):
            magnitude += 2 * e if i else 3 * e
        else:
            magnitude += 2 * get_magnitude(e) if i else 3 * get_magnitude(e)

    return magnitude


def to_string(num):
    return ''.join(str(e) for e in num)


if __name__ == '__main__':
    with open('input/day_18.txt', 'r') as f:
        assignment = parse_input(f.read())
        final_sum = reduce(lambda x, y: add(x, y), assignment)
        print(get_magnitude(final_sum))

        max_magnitude = 0
        for i in assignment:
            for j in assignment:
                if i == j:
                    continue
                max_magnitude = max(get_magnitude(add(i, j)), max_magnitude)
        print(max_magnitude)
