from dataclasses import dataclass
from io import TextIOBase
from typing import Self

from utils import stopwatch


@dataclass
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_reveal(cls, reveal: str) -> Self:
        cubes = {
            color: int(count)
            for count_color in reveal.split(", ")
            for count, color in [count_color.split()]
        }

        return CubeSet(**cubes)

    def __lt__(self, other: Self) -> bool:
        return (
            self.red < other.red and self.green < other.green and self.blue < other.blue
        )

    def __le__(self, other: Self) -> bool:
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    def __gt__(self, other: Self) -> bool:
        return (
            other.red < self.red and other.green < self.green and other.blue < self.blue
        )

    def __ge__(self, other: Self) -> bool:
        return (
            other.red <= self.red
            and other.green <= self.green
            and other.blue <= self.blue
        )


ParsedData = list[list[CubeSet]]


@stopwatch
def parse(input: TextIOBase) -> ParsedData:
    data = []

    for game in input:
        _, reveals = game.split(": ")
        data.append([CubeSet.from_reveal(reveal) for reveal in reveals.split("; ")])

    return data


@stopwatch
def part_1(data: ParsedData, bag: CubeSet = CubeSet(red=12, green=13, blue=14)) -> int:
    id_sum = 0

    for i, game in enumerate(data):
        if all(cube_set <= bag for cube_set in game):
            id_sum += i + 1

    return id_sum


if __name__ == "__main__":
    with open("input/day_02.txt", "r") as f:
        data = parse(f)
        print(part_1(data))
