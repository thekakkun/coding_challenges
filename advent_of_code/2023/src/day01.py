import io
from typing import Optional
import pprint

from utils import timer

ParsedInput = list[list[int]]


@timer
def part1(input: io.TextIOBase) -> int:
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
    }

    data = [
        (find_digit(line, digits), find_digit(line, digits, reverse=True))
        for line in input
    ]

    return calc_value(data)


@timer
def part2(input: io.TextIOBase) -> int:
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

    data = [
        (find_digit(line, digits), find_digit(line, digits, reverse=True))
        for line in input
    ]

    return calc_value(data)


def find_digit(
    line: str,
    digit_map: dict[str, int],
    reverse: Optional[bool] = False,
    starts_with: Optional[bool] = False,
) -> int:
    if "" in digit_map:
        return digit_map[""]

    if reverse:
        line = line[::-1]
        digit_map = {k[::-1]: v for k, v in digit_map.items()}

    for i, c in enumerate(line):
        next_digit_map = {k[1:]: v for k, v in digit_map.items() if k[0] == c}
        if next_digit_map:
            try:
                return find_digit(line[i + 1 :], next_digit_map, starts_with=True)
            except ValueError:
                continue
        elif starts_with:
            break

    raise ValueError("No digits in string.")


def calc_value(data: list[tuple[int, int]]) -> int:
    return sum(row[0] * 10 + row[1] for row in data)


if __name__ == "__main__":
    with open("input/day01.txt", "r") as f:
        print(part1(f))

    with open("input/day01.txt", "r") as f:
        print(part2(f))
