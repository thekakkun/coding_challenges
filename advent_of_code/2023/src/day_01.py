import io
from typing import Optional

from utils import stopwatch

ParsedData = list[str]


@stopwatch
def parse(input: io.TextIOBase) -> ParsedData:
    return list(input)


@stopwatch
def part_1(data: ParsedData) -> int:
    digits = {str(i): i for i in range(1, 10)}

    return sum(calibration_val(line, digits) for line in data)


@stopwatch
def part_2(data: ParsedData) -> int:
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
    return sum(calibration_val(line, digits) for line in data)


def calibration_val(line, digits) -> int:
    return 10 * find_digit(line, digits) + find_digit(line, digits, reverse=True)


def find_digit(
    line: str,
    digit_map: dict[str, int],
    reverse: Optional[bool] = False,
    match_beginning: Optional[bool] = False,
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
                return find_digit(line[i + 1 :], next_digit_map, match_beginning=True)
            except ValueError:
                continue
        elif match_beginning:
            break

    raise ValueError("No digits in string.")


if __name__ == "__main__":
    with open("input/day_01.txt", "r") as f:
        data = parse(f)
        print(part_1(data))
        print(part_2(data))
