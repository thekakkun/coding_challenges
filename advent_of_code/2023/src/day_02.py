from dataclasses import dataclass
from functools import reduce
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

    def min_required(self, other: Self) -> Self:
        return CubeSet(
            red=max(self.red, other.red),
            green=max(self.green, other.green),
            blue=max(self.blue, other.blue),
        )

    def power(self) -> int:
        return self.red * self.blue * self.green

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


ParsedData = dict[int, list[CubeSet]]


@stopwatch
def parse(input: TextIOBase) -> ParsedData:
    data = {}

    for game in input:
        game_id, reveals = game.split(": ")
        _, id = game_id.split(" ")
        data[int(id)] = [CubeSet.from_reveal(reveal) for reveal in reveals.split("; ")]

    return data


@stopwatch
def part_1(data: ParsedData, bag: CubeSet = CubeSet(red=12, green=13, blue=14)) -> int:
    return sum(
        id for id, game in data.items() if all(cube_set <= bag for cube_set in game)
    )


@stopwatch
def part_2(data: ParsedData) -> int:
    min_sets = [reduce(CubeSet.min_required, game) for game in data.values()]
    return sum(cubeset.power() for cubeset in min_sets)


if __name__ == "__main__":
    with open("input/day_02.txt", "r") as f:
        data = parse(f)
        print(part_1(data))
        print(part_2(data))
