from io import StringIO

from src.day_05 import *

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def test_parse():
    seeds, map_func = parse(StringIO(input))
    assert [map_func(seed) for seed in seeds] == [82, 43, 86, 35]


def test_part_2():
    seeds, map_func = parse(StringIO(input))

    assert part_2(seeds, map_func) == 46


def test_conversion():
    cat = Category()

    print(cat)

    assert False
