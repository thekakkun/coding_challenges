from io import TextIOBase
from itertools import chain
from typing import Callable, Iterable, Optional, Self
from dataclasses import dataclass, field
import bisect

from utils import stopwatch

MapTriple = tuple[int, int, int]
Seeds = Iterable[int]
MapFunc = Callable[[int], int]


@stopwatch
def parse(input: TextIOBase) -> tuple[Seeds, MapFunc]:
    seeds, *maps = input.read().split("\n\n")

    category_map_funcs = []

    for category_map in maps:
        _category_title, *category_definition = category_map.strip().split("\n")

        category_map_funcs.append(
            generate_category_map_func(
                parse_map_triple(triple_str) for triple_str in category_definition
            )
        )

    def seed_to_location(seed: int) -> int:
        for func in category_map_funcs:
            seed = func(seed)

        return seed

    return [int(seed) for seed in seeds.split()[1:]], seed_to_location


def parse_map_triple(triple: str) -> MapTriple:
    result = tuple(int(n) for n in triple.split())
    assert len(result) == 3

    return result


def generate_category_map_func(
    category_map: Iterable[MapTriple],
) -> Callable[[int], int]:
    """Return a function that maps from a source category value to a
    destination category value."""

    map_funcs = []

    for map_def in category_map:
        map_funcs.append(map_range_func(*map_def))

    def category_to_category(src: int) -> int:
        for map_f in map_funcs:
            result = map_f(src)

            if result is None:
                continue
            return result

        return src

    return category_to_category


def map_range_func(
    dest_start: int, src_start: int, range_len: int
) -> Callable[[int], Optional[int]]:
    """Return a function that maps from a source range to a destination range."""

    def range_to_range(src: int) -> Optional[int]:
        """Convert source number to destination number if within range, else None."""

        if src_start <= src < src_start + range_len:
            return src + (dest_start - src_start)

    return range_to_range


def seed_list_to_range(seeds: Seeds) -> Seeds:
    def seed_range():
        seeds_iter = iter(seeds)

        for seed in seeds_iter:
            range_len = next(seeds_iter)
            yield range(seed, seed + range_len)

    return chain.from_iterable(seed_range())


@dataclass
class Category:
    conversion_map: dict[int, int] = field(default_factory=lambda: {0: 0}, init=False)

    # def add_category(self, other: Self):
    #     for

    # def add_range(self, dest_start: int, src_start: int, range_len: int):
    #     keys = sorted(self.conversion_map)

    #     src_end = src_start + range_len
    #     range_shift = dest_start - src_start

    #     first_affected_ix = bisect.bisect_right(keys, src_start) - 1
    #     last_affected_ix = bisect.bisect_right(keys, src_end) - 1

    #     # Insert start of new range
    #     prev_range_shift = self.conversion_map[keys[first_affected_ix]]
    #     self.conversion_map[src_start] = range_shift + prev_range_shift
    #     # Restart previous range
    #     continue_shift = self.conversion_map[keys[last_affected_ix]]
    #     self.conversion_map[src_end] = continue_shift

    #     # Updates ranges affected by new range
    #     for i in keys[first_affected_ix + 1 : last_affected_ix + 1]:
    #         self.conversion_map[i] += range_shift

    # @dataclass
    # class MapRange:
    #     start: int
    #     end: int
    #     shift: int

    #     @classmethod
    #     def from_range_def(cls, range_def: str) -> Self:
    #         dest_start, src_start, range_len = (int(num) for num in range_def.split(" "))
    #         return cls(src_start, src_start + range_len - 1, dest_start - src_start)

    #     def merge(self, other: Self) -> list[Self]:
    #         if other.start < self.start:
    #             self, other = other, self

    #         if other.start < self.end:
    #             if other.end < self.end:  # fully contained
    #                 return [
    #                     MapRange(self.start, other.end - 1, self.shift),
    #                     MapRange(other.start, other.end, self.shift + other.shift),
    #                     MapRange(other.end + 1, self.end, self.shift),
    #                 ]
    #             elif self.end < other.end:  # overlap
    #                 return [
    #                     MapRange(self.start, other.end - 1, self.shift),
    #                     MapRange(other.start, self.end, self.shift + other.shift),
    #                     MapRange(self.end + 1, other.end, other.shift),
    #                 ]
    #             else:  # same end, shorter
    #                 return [
    #                     MapRange(self.start, other.end - 1, self.shift),
    #                     MapRange(other.start, other.end, self.shift + other.shift),
    #                 ]
    #         elif self.end < other.start:  # no overlap
    #             return [self, other]
    #         else:
    #             if other.end < self.end:  # same start, other shorter
    #                 return [
    #                     MapRange(self.start, other.end, self.shift + other.shift),
    #                     MapRange(other.end + 1, self.end, self.shift),
    #                 ]
    #             elif self.end < other.end:  # same start, other longer
    #                 return [
    #                     MapRange(self.start, self.end, self.shift + other.shift),
    #                     MapRange(self.end + 1, other.end, other.shift),
    #                 ]
    #             else:  # same start, same end
    #                 return [MapRange(self.start, self.end, self.shift + other.shift)]

    # # Ranges don't overlap at all:
    # if (self.end < other.start) or (other.end < self.start):
    #     return [self, other]

    # # Start of self overlaps end of other
    # elif other.start < self.start and self.start <= other.end < self.end:
    #     pass

    # # Start of other overlaps end of self
    # elif self.start < other.start and other.start <= self.end < other.end:
    #     pass

    # # One range completely within another
    # else:
    #     pass

    # if other.start < self.start:
    #     if other.end < self.start: # other before self
    #         pass
    #     else: # end of other overlaps start of self
    #         pass

    # # Other contained in self
    # if self.start < other.start and other.end < self.end:
    #     return [
    #         MapRange(self.start, other.start - 1, self.shift),
    #         MapRange(other.start, other.end, self.shift + other.shift),
    #         MapRange(other.start + 1, self.end, self.shift),
    #     ]

    # # Self contained in other
    # elif other.start < self.start and self.end < other.end:
    #     return [
    #         MapRange(other.start, self.start - 1, other.shift),
    #         MapRange(self.start, self.end, other.shift + self.shift),
    #         MapRange(self.start + 1, other.end, other.shift),
    #     ]

    # # Ranges don't overlap
    # else:
    #     return [self, other]

    # def convert(self, value: int) -> Optional[int]:
    #     if self.start <= value <= self.end:
    #         return value + self.shift


@stopwatch
def part_1(seeds: Seeds, map_func: MapFunc) -> int:
    return min(map_func(seed) for seed in seeds)


@stopwatch
def part_2(seeds: Seeds, map_func: MapFunc) -> int:
    seeds = seed_list_to_range(seeds)

    return min(map_func(seed) for seed in seeds)


if __name__ == "__main__":
    with open("input/day_05.txt", "r") as f:
        seeds, map_func = parse(f)
        print(part_1(seeds, map_func))
        print(part_2(seeds, map_func))
