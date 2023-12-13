from io import StringIO

from src.day_08 import *

input_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

input_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

input_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


def test_parse():
    instructions, network = parse(StringIO(input_1))

    assert instructions == "RL"

    assert network == {
        "AAA": Node(L="BBB", R="CCC"),
        "BBB": Node(L="DDD", R="EEE"),
        "CCC": Node(L="ZZZ", R="GGG"),
        "DDD": Node(L="DDD", R="DDD"),
        "EEE": Node(L="EEE", R="EEE"),
        "GGG": Node(L="GGG", R="GGG"),
        "ZZZ": Node(L="ZZZ", R="ZZZ"),
    }


def test_part_1():
    instructions_1, network_1 = parse(StringIO(input_1))
    assert part_1(instructions_1, network_1) == 2

    instructions_2, network_2 = parse(StringIO(input_2))
    assert part_1(instructions_2, network_2) == 6


def test_part_2():
    instructions, network = parse(StringIO(input_3))
    assert part_2(instructions, network) == 6
