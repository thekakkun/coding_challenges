from src.day01 import *
import io

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


def test_part1():
    assert part1(io.StringIO(input1)) == 142


def test_part2():
    assert part2(io.StringIO(input2)) == 281


def test_find_digit():
    digits = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
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
    assert [find_digit(line, digits) for line in io.StringIO(input2)] == [
        2,
        8,
        1,
        2,
        4,
        1,
        7,
    ]


def test_find_digit_reverse():
    digits = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
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
    assert [find_digit(line, digits, reverse=True) for line in io.StringIO(input2)] == [
        9,
        3,
        3,
        4,
        2,
        4,
        6,
    ]
