import math
import operator
from functools import reduce
from io import TextIOBase

from utils import stopwatch

Times = list[int]
Distances = list[int]


@stopwatch
def parse(input: TextIOBase) -> tuple[Times, Distances]:
    time_input, distance_input = next(input), next(input)

    _, times = time_input.split(":")
    _, distances = distance_input.split(":")

    return [int(t) for t in times.split()], [int(d) for d in distances.split()]


def hold_range(time: int, dist: int) -> tuple[float, float]:
    discriminant = math.sqrt(time**2 - 4 * dist)

    return (time - discriminant) / 2, (time + discriminant) / 2


def fix_input(data: Times | Distances) -> int:
    return int("".join(str(num) for num in data))


@stopwatch
def part_1(times, dists) -> int:
    hold_ranges = [hold_range(t, d) for t, d in zip(times, dists)]
    hold_margins = [
        math.ceil(end) - math.floor(start) - 1 for start, end in hold_ranges
    ]

    return reduce(operator.mul, hold_margins)


@stopwatch
def part_2(times, dists) -> int:
    time, dist = fix_input(times), fix_input(dists)
    start, end = hold_range(time, dist)

    return math.ceil(end) - math.floor(start) - 1


if __name__ == "__main__":
    with open("input/day_06.txt", "r") as f:
        times, dists = parse(f)
        print(part_1(times, dists))
        print(part_2(times, dists))
