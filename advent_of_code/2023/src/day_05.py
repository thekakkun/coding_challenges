from io import TextIOBase
from typing import Callable, Optional

from utils import stopwatch

Seeds = list[int]
RangeDef = tuple[int, int]
MapDef = tuple[int, int, int]
CategoryMap = list[MapDef]


@stopwatch
def parse(input: TextIOBase) -> tuple[Seeds, list[CategoryMap]]:
    seeds, *maps = input.read().split("\n\n")

    category_maps = []

    for map_ in maps:
        _, *map_ranges = map_.strip().split("\n")

        category_map = []

        for map_range in map_ranges:
            category_map.append([int(n) for n in map_range.split()])

        category_maps.append(category_map)

    return [int(seed) for seed in seeds.split()[1:]], category_maps


@stopwatch
def part_1(seeds: Seeds, category_maps: list[CategoryMap]) -> int:
    seed_ranges: list[RangeDef] = [(seed, 1) for seed in seeds]
    location_ranges = seed_to_location(category_maps)(seed_ranges)

    return min(range_start for range_start, _ in location_ranges)


@stopwatch
def part_2(seeds: Seeds, category_maps: list[CategoryMap]) -> int:
    seed_iter = iter(seeds)
    seed_ranges = [(seed, next(seed_iter)) for seed in seed_iter]

    location_ranges = seed_to_location(category_maps)(seed_ranges)

    return min(range_start for range_start, _ in location_ranges)


def seed_to_location(
    category_maps: list[CategoryMap],
) -> Callable[[list[RangeDef]], list[RangeDef]]:
    category_map_funcs = [
        category_to_category(category_map) for category_map in category_maps
    ]

    def _f(seed_ranges: list[RangeDef]) -> list[RangeDef]:
        for func in category_map_funcs:
            seed_ranges = func(seed_ranges)

        return seed_ranges

    return _f


def category_to_category(
    category_map: CategoryMap,
) -> Callable[[list[RangeDef]], list[RangeDef]]:
    """Return a function that maps from a source category range to a
    destination category range."""
    map_funcs = [range_to_range(range_def) for range_def in category_map]

    def _f(seed_ranges: list[RangeDef]) -> list[RangeDef]:
        result = []

        for map_func in map_funcs:
            seed_range_queue = []

            while seed_ranges:
                seed_range = seed_ranges.pop()
                converted, unconverted = map_func(seed_range)

                if converted:
                    result.append(converted)
                seed_range_queue.extend(unconverted)

            seed_ranges = seed_range_queue

        return result + seed_ranges

    return _f


def range_to_range(
    range_def: MapDef,
) -> Callable[[RangeDef], tuple[Optional[RangeDef], list[RangeDef]]]:
    """Returns a function that maps from a source range to destination ranges"""

    dest_start, src_start, range_len = range_def

    src_end = src_start + range_len - 1
    shift = dest_start - src_start

    def _f(seed_range: RangeDef) -> tuple[Optional[RangeDef], list[RangeDef]]:
        """Splits a map range into converted and unconverted sections, depending on how they overlap."""
        seed_start, seed_range_len = seed_range
        seed_end = seed_start + seed_range_len - 1

        overlap_start, overlap_end = (
            max(src_start, seed_start),
            min(src_end, seed_end),
        )

        converted = None
        unconverted = []
        if overlap_start <= overlap_end:
            converted = (overlap_start + shift, overlap_end - overlap_start + 1)

            if seed_start < overlap_start:
                unconverted.append((seed_start, overlap_start - seed_start))
            elif overlap_end < seed_end:
                unconverted.append((overlap_end + 1, seed_end - overlap_end))

        else:
            unconverted.append(seed_range)

        return converted, unconverted

    return _f


if __name__ == "__main__":
    with open("input/day_05.txt", "r") as f:
        seeds, category_maps = parse(f)
        print(part_1(seeds, category_maps))
        print(part_2(seeds, category_maps))
