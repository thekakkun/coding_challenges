from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import InitVar, dataclass, field
from io import TextIOBase
from typing import Self, Literal

from utils import stopwatch

Coord = tuple[int, int]
Direction = Literal["north", "south", "east", "west"]


def look(coord: Coord, direction: Direction) -> Coord:
    i, j = coord
    if direction == "north":
        return (i - 1, j)
    elif direction == "south":
        return (i + 1, j)
    elif direction == "east":
        return (i, j + 1)
    elif direction == "west":
        return (i, j - 1)
    else:
        raise Exception(f"Unknown direction: {direction}")


@dataclass
class Pipe(ABC):
    coord: Coord

    @abstractmethod
    def travel(self, going: Direction) -> Direction:
        ...

    @abstractmethod
    def lhs(self, going: Direction) -> list[Coord]:
        ...

    @abstractmethod
    def rhs(self, going: Direction) -> list[Coord]:
        ...


class NSPipe(Pipe):
    def travel(self, going: Direction) -> Direction:
        if going == "north":
            return "north"
        elif going == "south":
            return "south"
        else:
            raise Exception(f"Can't enter from direction: {going}")

    def lhs(self, going: Direction) -> list[Coord]:
        if going == "north":
            return [look(self.coord, "west")]
        elif going == "south":
            return [look(self.coord, "east")]
        else:
            raise Exception(f"Can't enter from direction: {going}")

    def rhs(self, going: Direction) -> list[Coord]:
        if going == "north":
            return [look(self.coord, "east")]
        elif going == "south":
            return [look(self.coord, "west")]
        else:
            raise Exception(f"Can't enter from direction: {going}")


class EWPipe(Pipe):
    def travel(self, going: Direction) -> Direction:
        if going == "east":
            return "east"
        elif going == "west":
            return "west"
        else:
            raise Exception("Can't enter from that direction.")

    def lhs(self, going: Direction) -> list[Coord]:
        if going == "east":
            return [look(self.coord, "north")]
        elif going == "west":
            return [look(self.coord, "south")]
        else:
            raise Exception("Can't enter from that direction.")

    def rhs(self, going: Direction) -> list[Coord]:
        if going == "east":
            return [look(self.coord, "south")]
        elif going == "west":
            return [look(self.coord, "north")]
        else:
            raise Exception("Can't enter from that direction.")


class NEPipe(Pipe):
    def travel(self, going: Direction) -> Direction:
        if going == "south":
            return "east"
        elif going == "west":
            return "north"
        else:
            raise Exception("Can't enter from that direction.")

    def lhs(self, going: Direction) -> list[Coord]:
        if going == "south":
            return []
        elif going == "west":
            return [look(self.coord, "south"), look(self.coord, "west")]
        else:
            raise Exception("Can't enter from that direction.")

    def rhs(self, going: Direction) -> list[Coord]:
        if going == "south":
            return [look(self.coord, "south"), look(self.coord, "west")]
        elif going == "west":
            return []
        else:
            raise Exception("Can't enter from that direction.")


class NWPipe(Pipe):
    def travel(self, going: Direction) -> Direction:
        if going == "south":
            return "west"
        elif going == "east":
            return "north"
        else:
            raise Exception("Can't enter from that direction.")

    def lhs(self, going: Direction) -> list[Coord]:
        if going == "south":
            return [look(self.coord, "south"), look(self.coord, "east")]
        elif going == "east":
            return []
        else:
            raise Exception("Can't enter from that direction.")

    def rhs(self, going: Direction) -> list[Coord]:
        if going == "south":
            return []
        elif going == "east":
            return [look(self.coord, "south"), look(self.coord, "east")]
        else:
            raise Exception("Can't enter from that direction.")


class SWPipe(Pipe):
    def travel(self, going: Direction) -> Direction:
        if going == "north":
            return "west"
        elif going == "east":
            return "south"
        else:
            raise Exception("Can't enter from that direction.")

    def lhs(self, going: Direction) -> list[Coord]:
        if going == "north":
            return []
        elif going == "east":
            return [look(self.coord, "north"), look(self.coord, "east")]
        else:
            raise Exception("Can't enter from that direction.")

    def rhs(self, going: Direction) -> list[Coord]:
        if going == "north":
            return [look(self.coord, "north"), look(self.coord, "east")]
        elif going == "east":
            return []
        else:
            raise Exception("Can't enter from that direction.")


class SEPipe(Pipe):
    def travel(self, going: Direction) -> Direction:
        if going == "north":
            return "east"
        elif going == "west":
            return "south"
        else:
            raise Exception("Can't enter from that direction.")

    def lhs(self, going: Direction) -> list[Coord]:
        if going == "north":
            return []
        elif going == "west":
            return [look(self.coord, "north"), look(self.coord, "west")]
        else:
            raise Exception("Can't enter from that direction.")

    def rhs(self, going: Direction) -> list[Coord]:
        if going == "north":
            return [look(self.coord, "north"), look(self.coord, "west")]
        elif going == "west":
            return []
        else:
            raise Exception("Can't enter from that direction.")


@dataclass
class Field:
    input: InitVar[TextIOBase]

    start_coord: Coord = field(init=False)
    start_dir: Direction = field(init=False)
    pipes: dict[Coord, Pipe] = field(default_factory=dict)

    def __post_init__(self, input: TextIOBase):
        for i, line in enumerate(input):
            for j, char in enumerate(line.strip()):
                if char == "S":
                    self.start_coord = (i, j)
                elif char == ".":
                    continue
                else:
                    self.add_pipe(char, (i, j))

        # Check to see what direction you can travel to from the start.
        directions: list[Direction] = ["north", "south", "east", "west"]
        for direction in directions:
            try:
                next_coord = look(self.start_coord, direction)
                self.pipes[next_coord].travel(direction)
                self.start_dir = direction
                break
            except:
                continue

    def add_pipe(
        self,
        pipe_type: str,
        coord: Coord,
    ):
        type_to_pipe = {
            "|": NSPipe(coord),
            "-": EWPipe(coord),
            "L": NEPipe(coord),
            "J": NWPipe(coord),
            "7": SWPipe(coord),
            "F": SEPipe(coord),
        }

        self.pipes[coord] = type_to_pipe[pipe_type]


@stopwatch
def parse(input: TextIOBase) -> Field:
    return Field(input)


@stopwatch
def part_1(field: Field) -> int:
    next_coord = look(field.start_coord, field.start_dir)
    next_dir = field.start_dir
    loop_len = 1

    while next_coord != field.start_coord:
        loop_len += 1
        next_dir = field.pipes[next_coord].travel(next_dir)
        next_coord = look(next_coord, next_dir)

    return loop_len // 2


if __name__ == "__main__":
    with open("input/day_10.txt", "r") as f:
        field = parse(f)
        print(part_1(field))
        # print(part_2(sequences))
