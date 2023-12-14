from collections import defaultdict
from dataclasses import dataclass, field
from io import TextIOBase
from typing import Self

from utils import stopwatch

Coord = tuple[int, int]


@dataclass
class Field:
    start: Coord = field(init=False)
    pipes: dict[Coord, list[Coord]] = field(default_factory=lambda: defaultdict(list))

    @classmethod
    def from_input(cls, input: TextIOBase) -> Self:
        field = cls()

        for i, line in enumerate(input):
            for j, char in enumerate(line.strip()):
                if char == "S":
                    field.start = (i, j)
                elif char == ".":
                    continue
                else:
                    field.add_pipe(char, (i, j))

        return field

    def add_pipe(self, p_type: str, coord: Coord):
        pipe_type = {
            "|": lambda i, j: [(i - 1, j), (i + 1, j)],
            "-": lambda i, j: [(i, j - 1), (i, j + 1)],
            "L": lambda i, j: [(i - 1, j), (i, j + 1)],
            "J": lambda i, j: [(i - 1, j), (i, j - 1)],
            "7": lambda i, j: [(i + 1, j), (i, j - 1)],
            "F": lambda i, j: [(i + 1, j), (i, j + 1)],
        }

        self.pipes[coord] = pipe_type[p_type](*coord)

    def find_loop(self) -> list[Coord]:
        visited = [self.start]

        # Find the next pipe section from the start pipe
        (s_i, s_j) = self.start
        for coord in [(s_i - 1, s_j), (s_i + 1, s_j), (s_i, s_j - 1), (s_i, s_j + 1)]:
            if self.start in self.pipes.get(coord, []):
                visited.append(coord)
                break

        while visited[-1] != self.start:
            *_, previous, current = visited
            next_pipe = (  # Could optimize this by checking direction of travel
                self.pipes[current][0]
                if self.pipes[current][1] == previous
                else self.pipes[current][1]
            )
            visited.append(next_pipe)

        return visited


@stopwatch
def parse(input: TextIOBase) -> Field:
    return Field.from_input(input)


@stopwatch
def part_1(field: Field) -> int:
    loop_path = field.find_loop()
    return len(loop_path) // 2


if __name__ == "__main__":
    with open("input/day_10.txt", "r") as f:
        field = parse(f)
        print(part_1(field))
        # print(part_2(sequences))
