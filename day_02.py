# https://adventofcode.com/2021/day/2

def navigate_1(commands):
    h = 0
    d = 0

    for c in commands:
        (direction, units) = c.split(' ')
        units = int(units)

        if direction == 'forward':
            h += units
            continue
        elif direction == 'up':
            d -= units
            continue
        elif direction == 'down':
            d += units
            continue

    return h * d


def navigate_2(commands):
    h = 0
    d = 0
    a = 0

    for c in commands:
        (direction, units) = c.split(' ')
        units = int(units)

        if direction == 'forward':
            h += units
            d += a * units
            continue
        elif direction == 'up':
            a -= units
            continue
        elif direction == 'down':
            a += units
            continue

    return h * d


with open('./input/day_02.txt') as f:
    commands = f.read().splitlines()
    print(navigate_1(commands))
    print(navigate_2(commands))
