from io import StringIO

from src.day_07 import *

input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_parse():
    hands = parse(StringIO(input))
    assert hands == [
        Hand("32T3K", 765),
        Hand("T55J5", 684),
        Hand("KK677", 28),
        Hand("KTJJT", 220),
        Hand("QQQJA", 483),
    ]
    assert [hand.kind for hand in hands] == ["1P", "3K", "2P", "2P", "3K"]


def test_part_1():
    hands = parse(StringIO(input))
    assert part_1(hands) == 6440


def test_use_joker():
    hands = parse(StringIO(input))
    for hand in hands:
        hand.use_joker = True

    assert [hand.kind for hand in hands] == ["1P", "4K", "2P", "4K", "4K"]


def test_part_2():
    hands = parse(StringIO(input))
    assert part_2(hands) == 5905
