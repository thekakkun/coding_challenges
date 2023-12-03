from io import StringIO

from src.day_03 import *

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_parse():
    symbols = [
        {"coord": (1, 3), "val": "*"},
        {"coord": (3, 6), "val": "#"},
        {"coord": (4, 3), "val": "*"},
        {"coord": (5, 5), "val": "+"},
        {"coord": (8, 3), "val": "$"},
        {"coord": (8, 5), "val": "*"},
    ]

    schematic = Schematic(StringIO(input))
    assert schematic.symbols == symbols

    # too lazy to check numbers...


def test_part_1():
    schematic = Schematic(StringIO(input))
    assert part_1(schematic) == 4361


def test_part_2():
    schematic = Schematic(StringIO(input))
    assert part_2(schematic) == 467835
