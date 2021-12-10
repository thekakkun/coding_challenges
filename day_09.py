# https://adventofcode.com/2021/day/9

import functools


def get_lower_than(heightmap):
    rows, cols = len(heightmap), len(heightmap[0])
    lower_than = [[set() for _ in range(cols)] for _ in range(rows)]
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for r in range(rows):
        for c in range(cols):
            if heightmap[r][c] == 9:
                continue
            elif heightmap[r][c] == 0:
                lower_than[r][c].update(
                    tuple(sum(x) for x in zip((r, c), d))
                    for d in directions)
            else:
                for (d_r, d_c) in directions:
                    if (
                        (r + d_r) not in range(rows) or
                        (c + d_c) not in range(cols) or
                        heightmap[r][c] < heightmap[r + d_r][c + d_c]
                    ):
                        lower_than[r][c].add((r + d_r, c + d_c))

    return lower_than


def get_basin(heightmap, low_point, lower_than):
    rows, cols = len(heightmap), len(heightmap[0])
    lower_than = get_lower_than(heightmap)
    (lp_r, lp_c) = low_point

    basin = set((low_point,))
    frontier = list(lower_than[lp_r][lp_c])
    visited = set()

    while frontier:
        print(visited)
        (p_r, p_c) = frontier.pop()
        if (p_r, p_c) in visited:
            continue
        elif (
            (p_r, p_c) in basin or
            p_r not in range(rows) or
            p_c not in range(cols) or
            heightmap[p_r][p_c] == 9
        ):
            visited.add((p_r, p_c))
            continue
        else:
            basin.add((p_r, p_c))
            visited.add((p_r, p_c))

            frontier += list(lower_than[p_r][p_c])

    return basin


def get_risk_level(heightmap):
    rows, cols = len(heightmap), len(heightmap[0])
    lower_than = get_lower_than(heightmap)

    return sum(heightmap[r][c] + 1
               for r in range(rows)
               for c in range(cols)
               if len(lower_than[r][c]) == 4
               )


def find_basins(heightmap):
    rows, cols = len(heightmap), len(heightmap[0])
    lower_than = get_lower_than(heightmap)

    low_points = [(r, c)
                  for r in range(rows)
                  for c in range(cols)
                  if len(lower_than[r][c]) == 4
                  ]
    basin_sizes = [len(get_basin(heightmap, lp, lower_than))
                   for lp in low_points]

    return functools.reduce(
        lambda x, y: x * y,
        sorted(basin_sizes, reverse=True)[:3]
    )


with open('input/day_09.txt', 'r') as f:
    heightmap = tuple(
        tuple(int(y) for y in x)
        for x in f.read().strip().splitlines()
    )

    print(get_risk_level(heightmap))
    print(find_basins(heightmap))
