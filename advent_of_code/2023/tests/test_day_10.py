from io import StringIO

from src.day_10 import *

input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""


def test_parse():
    field = parse(StringIO(input))

    assert field.start == (2, 0)


def test_part_1():
    field = parse(StringIO(input))

    assert part_1(field) == 8
