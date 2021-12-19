# https://adventofcode.com/2021/day/5


import itertools


def parse_input(text):
    return tuple(
        tuple(
            tuple(int(z) for z in y.split(',')
                  ) for y in x.split(' -> ')
        ) for x in text.splitlines()
    )


def map_vents(vents):
    vent_map = {}

    for vent in vents:
        ((x1, y1), (x2, y2)) = vent
        x_range = range(x1, x2 + 1) if x1 <= x2 else range(x1, x2-1, -1)
        y_range = range(y1, y2 + 1) if y1 <= y2 else range(y1, y2-1, -1)

        for vent_loc in itertools.zip_longest(
            x_range, y_range, fillvalue=min(x_range, y_range, key=len)[0]
        ):
            vent_map[vent_loc] = vent_map.get(vent_loc, 0) + 1

    return vent_map


def find_vents_1(vents):
    vents = (x for x in vents if x[0][0] == x[1][0] or x[0][1] == x[1][1])
    vent_map = map_vents(vents)

    return sum(1 for _, v in vent_map.items() if 2 <= v)


def find_vents_2(vents):
    vent_map = map_vents(vents)

    return sum(1 for _, v in vent_map.items() if 2 <= v)


if __name__ == '__main__':
    with open('input/day_05.txt', 'r') as f:
        text = f.read().strip()
        vents = parse_input(text)

        print(find_vents_1(vents))
        print(find_vents_2(vents))
