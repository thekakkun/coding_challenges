# https://adventofcode.com/2021/day/22

import re
from functools import reduce


def parse_input(text):
    text = text.strip()
    pattern = r'(?:(-?\d+)\.{2}(-?\d+))'
    steps = []

    for line in text.splitlines():
        (switch, coordinates) = line.split()
        switch = 1 if (switch == 'on') else 0
        coordinates = tuple(
            (int(c1), int(c2)+1)
            for c1, c2 in re.findall(pattern, coordinates)
        )
        steps.append((switch, coordinates,))

    return steps


def intersects(cube1, cube2):
    (c1_x, c1_y, c1_z) = cube1
    (c2_x, c2_y, c2_z) = cube2

    if max(c2_x) < min(c1_x):
        return False
    elif max(c1_x) < min(c2_x):
        return False
    elif max(c2_y) < min(c1_y):
        return False
    elif max(c1_y) < min(c2_y):
        return False
    elif max(c2_z) < min(c1_z):
        return False
    elif max(c1_z) < min(c2_z):
        return False
    else:
        return True


def get_intersection(cube1, cube2):
    (c1_x, c1_y, c1_z) = cube1
    (c2_x, c2_y, c2_z) = cube2

    return (
        sorted([max(min(c1_x), min(c2_x)), min(max(c1_x), max(c2_x))]),
        sorted([max(min(c1_y), min(c2_y)), min(max(c1_y), max(c2_y))]),
        sorted([max(min(c1_z), min(c2_z)), min(max(c1_z), max(c2_z))])
    )


def subtract(cube1, cube2):
    (c1_x, c1_y, c1_z) = cube1 = [list(x) for x in cube1]
    (ci_x, ci_y, ci_z) = get_intersection(cube1, cube2)

    remainders = []

    if c1_x[0] < ci_x[0]:
        remainders.append(((c1_x[0], ci_x[0]), tuple(c1_y), tuple(c1_z)))
        c1_x[0] = ci_x[0]
    if ci_x[1] < c1_x[1]:
        remainders.append(((ci_x[1], c1_x[1]), tuple(c1_y), tuple(c1_z)))
        c1_x[1] = ci_x[1]
    if c1_y[0] < ci_y[0]:
        remainders.append((tuple(c1_x), (c1_y[0], ci_y[0]), tuple(c1_z)))
        c1_y[0] = ci_y[0]
    if ci_y[1] < c1_y[1]:
        remainders.append((tuple(c1_x), (ci_y[1], c1_y[1]), tuple(c1_z)))
        c1_y[1] = ci_y[1]
    if c1_z[0] < ci_z[0]:
        remainders.append((tuple(c1_x), tuple(c1_y), (c1_z[0], ci_z[0])))
        c1_z[0] = ci_z[0]
    if ci_z[1] < c1_z[1]:
        remainders.append((tuple(c1_x), tuple(c1_y), (ci_z[1], c1_z[1])))
        c1_z[1] = ci_z[1]

    return remainders


def vol(cube):
    return reduce(
        lambda x, y: x * y,
        (abs(a - b) for a, b in cube)
    )


def init(steps, init_range=((-50, 51), (-50, 51), (-50, 51),)):
    grid = {}

    for step in steps:
        (switch, xyz_range) = step
        (x_range, y_range, z_range) = (
            set(range(*r1)) & set(range(*r2))
            for r1, r2 in zip(init_range, xyz_range)
        )

        if not all((x_range, y_range, z_range)):
            continue

        grid.update({
            (x, y, z): switch
            for x in x_range
            for y in y_range
            for z in z_range
        })

    return sum(grid.values())


def boot(steps):
    on_cube_list = set()

    for step in steps:
        (switch, cube) = step

        for on_cube in (c for c in list(on_cube_list) if intersects(c, cube)):
            on_cube_list.remove(on_cube)
            on_cube_list.update(subtract(on_cube, cube))

        if switch:
            on_cube_list.add(cube)

    return sum(map(vol, on_cube_list))


if __name__ == '__main__':
    with open('input/day_22.txt', 'r') as f:
        steps = parse_input(f.read())
        print(init(steps))
        print(boot(steps))
