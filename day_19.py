# https://adventofcode.com/2021/day/19

import re


def parse_input(text):
    report = {}
    for scanner in text.strip().split('\n\n'):
        scanner = scanner.splitlines()
        n = int(re.findall(r'\d+', scanner[0])[0])

        coordinates = set(
            tuple(map(int, re.findall(r'-?\d+', loc)))
            for loc in scanner[1:])

        report[n] = coordinates
    return report


def iter_rotate(beacons):
    rotations = (
        ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        ((1, 0, 0), (0, 0, -1), (0, 1, 0)),
        ((1, 0, 0), (0, -1, 0), (0, 0, -1)),
        ((1, 0, 0), (0, 0, 1), (0, -1, 0)),
        ((0, -1, 0), (1, 0, 0), (0, 0, 1)),
        ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
        ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
        ((-1, 0, 0), (0, -1, 0), (0, 0, 1)),
        ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
        ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
        ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),
        ((0, 1, 0), (-1, 0, 0), (0, 0, 1)),
        ((0, 0, 1), (-1, 0, 0), (0, -1, 0)),
        ((0, -1, 0), (-1, 0, 0), (0, 0, -1)),
        ((0, 0, -1), (-1, 0, 0), (0, 1, 0)),
        ((0, 0, -1), (0, 1, 0), (1, 0, 0)),
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ((0, 0, 1), (0, -1, 0), (1, 0, 0)),
        ((0, -1, 0), (0, 0, -1), (1, 0, 0)),
        ((0, 0, -1), (0, -1, 0), (-1, 0, 0)),
        ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
        ((0, 0, 1), (0, 1, 0), (-1, 0, 0)),
        ((0, 1, 0), (0, 0, -1), (-1, 0, 0))
    )

    for R in rotations:
        yield set(rotate(b, R) for b in beacons)


def rotate(coordinate, R):
    return tuple(
        sum((a * b) for a, b in zip(R[r], coordinate))
        for r in range(len(coordinate))
    )


def add(b_r, b_o):
    return tuple(sum(x) for x in zip(b_r, b_o))


def sub(b_a, b_r):
    return tuple(a-r for a, r in zip(b_a, b_r))


def find_offset(abs_beacons, rel_beacons, overlap=12):
    for b_a in sorted(abs_beacons):
        for b_r in sorted(rel_beacons)[:-overlap+1]:
            offset = sub(b_a, b_r)
            rel_beacons_absoluted = set(add(b, offset) for b in rel_beacons)
            if overlap <= len(abs_beacons & rel_beacons_absoluted):
                return (offset, rel_beacons_absoluted)
    return ()


def create_map(report):
    full_map = {(0, 0, 0): report.pop(0)}
    unfixed_scanners = list(report.keys())
    checked = set()

    while unfixed_scanners:
        s = unfixed_scanners.pop(0)
        s_fixed = False

        for fixed_beacon in list(full_map):
            if s_fixed:
                break
            elif (s, fixed_beacon,) in checked:
                continue

            for unfixed_beacon in iter_rotate(report[s]):
                offset = find_offset(full_map[fixed_beacon], unfixed_beacon)
                if offset:
                    s_fixed = True
                    full_map[offset[0]] = offset[1]
                    break
            else:
                checked.add((s, fixed_beacon))
        else:
            if not s_fixed:
                unfixed_scanners.append(s)

    return set(full_map.keys()), set().union(*full_map.values())


def get_furthest(scanners):
    furthest = max(
        sum(abs(x) for x in sub(s1, s2))
        for s1 in scanners
        for s2 in scanners
        if s1 != s2
    )
    return furthest


if __name__ == '__main__':
    with open('input/day_19.txt', 'r') as f:
        report = parse_input(f.read())
        scanners, beacons = create_map(report)
        print(len(beacons))
        print(get_furthest(scanners))
