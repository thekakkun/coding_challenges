from io import StringIO

from src.day_09 import *

input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def test_parse():
    assert parse(StringIO(input)) == [
        [0, 3, 6, 9, 12, 15],
        [1, 3, 6, 10, 15, 21],
        [10, 13, 16, 21, 30, 45],
    ]


def test_part_1():
    data = parse(StringIO(input))

    assert part_1(data) == 114

def test_part_2():
    data = parse(StringIO(input))

    assert part_2(data) == 2
