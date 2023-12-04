from io import StringIO

from src.day_04 import *

input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def test_parse():
    assert parse(StringIO(input)) == [
        ScratchCard(set([41, 48, 83, 86, 17]), set([83, 86, 6, 31, 17, 9, 48, 53])),
        ScratchCard(set([13, 32, 20, 16, 61]), set([61, 30, 68, 82, 17, 32, 24, 19])),
        ScratchCard(set([1, 21, 53, 59, 44]), set([69, 82, 63, 72, 16, 21, 14, 1])),
        ScratchCard(set([41, 92, 73, 84, 69]), set([59, 84, 76, 51, 58, 5, 54, 83])),
        ScratchCard(set([87, 83, 26, 28, 32]), set([88, 30, 70, 12, 93, 22, 82, 36])),
        ScratchCard(set([31, 18, 13, 56, 72]), set([74, 77, 10, 23, 35, 67, 36, 11])),
    ]


def test_part_1():
    data = parse(StringIO(input))

    assert tuple(card.points for card in data) == (8, 2, 2, 1, 0, 0)
    assert part_01(data) == 13


def test_part_2():
    data = parse(StringIO(input))
    assert part_02(data) == 30
