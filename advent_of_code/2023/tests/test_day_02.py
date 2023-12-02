from io import StringIO

from src.day_02 import *

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def test_parse():
    assert parse(StringIO(input)) == [
        [CubeSet(blue=3, red=4), CubeSet(red=1, green=2, blue=6), CubeSet(green=2)],
        [
            CubeSet(blue=1, green=2),
            CubeSet(green=3, blue=4, red=1),
            CubeSet(green=1, blue=1),
        ],
        [
            CubeSet(green=8, blue=6, red=20),
            CubeSet(blue=5, red=4, green=13),
            CubeSet(green=5, red=1),
        ],
        [
            CubeSet(green=1, red=3, blue=6),
            CubeSet(green=3, red=6),
            CubeSet(green=3, blue=15, red=14),
        ],
        [CubeSet(red=6, blue=1, green=3), CubeSet(blue=2, red=1, green=2)],
    ]

def test_part_1():
    data = parse(StringIO(input))

    assert part_1(data) == 8