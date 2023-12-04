import math
import re
from dataclasses import dataclass
from io import TextIOBase

from utils import stopwatch


@dataclass
class ScratchCard:
    numbers: set[int]
    winning_numbers: set[int]

    @property
    def matches(self):
        return self.numbers & self.winning_numbers

    @property
    def points(self):
        return 2 ** (len(self.matches) - 1) if self.matches else 0


@stopwatch
def parse(input: TextIOBase) -> list[ScratchCard]:
    data = []

    for line in input:
        _, numbers, winning_numbers = re.split(r": | \| ", line)

        data.append(
            ScratchCard(
                set(int(n) for n in numbers.split()),
                set(int(n) for n in winning_numbers.split()),
            )
        )

    return data


@stopwatch
def part_01(data: list[ScratchCard]) -> int:
    return sum(card.points for card in data)


@stopwatch
def part_02(data: list[ScratchCard]) -> int:
    spawns = []

    for card in data[::-1]:
        spawn = sum(spawns[-len(card.matches) : :] if card.matches else []) + 1

        spawns.append(spawn)

    return sum(spawns)


if __name__ == "__main__":
    with open("input/day_04.txt", "r") as f:
        data = parse(f)
        print(part_01(data))
        print(part_02(data))
