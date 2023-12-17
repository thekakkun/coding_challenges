from io import StringIO

from src.day_10 import *

input_1 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

input_2 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""


def test_parse():
    field = parse(StringIO(input_1))
    assert field.start_coord == (2, 0)


def test_part_1():
    field = parse(StringIO(input_1))
    assert part_1(field) == 8

# def test_part_2():
#     field = parse(StringIO(input_2))
#     assert part_2(field) == 8
