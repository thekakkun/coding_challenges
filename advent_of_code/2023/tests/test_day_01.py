from io import StringIO

from src.day_01 import *

input1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def test_part_1():
    assert part_1(StringIO(input1)) == 142


def test_part_2():
    assert part_2(StringIO(input2)) == 281


def test_find_digit():
    digits = {str(i): i for i in range(1, 10)} | {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    assert [find_digit(line, digits) for line in StringIO(input2)] == [
        2,
        8,
        1,
        2,
        4,
        1,
        7,
    ]


def test_find_digit_reverse():
    digits = {str(i): i for i in range(1, 10)} | {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    assert [find_digit(line, digits, reverse=True) for line in StringIO(input2)] == [
        9,
        3,
        3,
        4,
        2,
        4,
        6,
    ]
