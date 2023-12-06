from io import StringIO

from src.day_06 import *

input = """Time:      7  15   30
Distance:  9  40  200
"""


def test_parse():
    times, dists = parse(StringIO(input))
    assert times == [7, 15, 30]
    assert dists == [9, 40, 200]


def test_part_1():
    times, dists = parse(StringIO(input))
    assert part_1(times, dists) == 288


def test_part_2():
    times, dists = parse(StringIO(input))
    assert part_2(times, dists) == 71503
