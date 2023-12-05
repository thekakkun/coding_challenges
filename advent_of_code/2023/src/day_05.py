from io import TextIOBase
from typing import Callable, Optional

from utils import stopwatch

MapTriple = tuple[int, int, int]
Seeds = list[int]
MapFunc = Callable[[int], int]


@stopwatch
def parse(input: TextIOBase) -> tuple[Seeds, MapFunc]:
    seeds, *maps = input.read().split("\n\n")

    category_map_funcs = []

    for category_map in maps:
        _category_title, *category_definition = category_map.strip().split("\n")

        category_map = [
            parse_map_triple(triple_str) for triple_str in category_definition
        ]

        category_map_funcs.append(generate_category_map_func(category_map))

    def seed_to_location(seed: int) -> int:
        for func in category_map_funcs:
            seed = func(seed)

        return seed

    return [int(seed) for seed in seeds.split()[1:]], seed_to_location


def parse_map_triple(triple: str) -> MapTriple:
    result = tuple(int(n) for n in triple.split())
    assert len(result) == 3

    return result


def generate_category_map_func(category_map: list[MapTriple]) -> Callable[[int], int]:
    """Return a function that maps from a source category value to a
    destination category value."""
    map_funcs = []

    for map_def in category_map:
        map_funcs.append(generate_range_map_func(*map_def))

    def category_to_category(src: int) -> int:
        for map_f in map_funcs:
            if map_f(src):
                return map_f(src)

        return src

    return category_to_category


def generate_range_map_func(
    dest_start: int, src_start: int, range_len: int
) -> Callable[[int], Optional[int]]:
    """Return a function that maps from a source range to a destination range."""

    def range_to_range(src: int) -> Optional[int]:
        """Convert source number to destination number if within range, else None."""
        if src in range(src_start, src_start + range_len):
            return src + (dest_start - src_start)

    return range_to_range


@stopwatch
def part_1(seeds: Seeds, map_func: MapFunc) -> int:
    return min(map_func(seed) for seed in seeds)


if __name__ == "__main__":
    with open("input/day_05.txt", "r") as f:
        seeds, map_func = parse(f)
        print(part_1(seeds, map_func))
