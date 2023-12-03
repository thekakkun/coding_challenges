from collections import defaultdict
from dataclasses import InitVar, dataclass, field
from functools import reduce
from io import TextIOBase
from typing import TypedDict

from utils import stopwatch

Point = tuple[int, int]
PointHash = tuple[int, int]


class Number(TypedDict):
    bb: tuple[Point, Point]
    val: int


class Symbol(TypedDict):
    coord: Point
    val: str


@dataclass
class Schematic:
    input: InitVar[TextIOBase]

    # Objects in the schematic
    numbers: list[Number] = field(default_factory=list, init=False)
    symbols: list[Symbol] = field(default_factory=list, init=False)

    # Uses a spatial hash to chunk together nearby numbers into cells.
    bucket: defaultdict[PointHash, set[int]] = field(
        default_factory=lambda: defaultdict(set)
    )
    cell_size: int = 5

    def __post_init__(self, input: TextIOBase):
        temp_num = 0
        temp_locs = []

        for i, line in enumerate(input):
            for j, c in enumerate(line):
                if c.isdecimal():
                    temp_num = temp_num * 10 + int(c)
                    temp_locs.append((i, j))
                else:
                    if temp_locs:
                        self.insert_number(temp_num, temp_locs)
                        temp_num = 0
                        temp_locs = []

                    if c not in [".", "\n"]:
                        self.symbols.append({"coord": (i, j), "val": c})

    def point_hash(self, point: Point) -> PointHash:
        """Turns point into a hash.

        In effect, lowers the resolution of the schematic into pixels of size `cell_size`.
        """
        return (point[0] // self.cell_size, point[1] // self.cell_size)

    def insert_number(self, value: int, points: list[Point]):
        self.numbers.append({"bb": (points[0], points[-1]), "val": value})
        id = len(self.numbers) - 1

        for point in points:
            self.bucket[self.point_hash(point)].add(id)

    def get_cells(self, point: Point) -> set[PointHash]:
        """Get cells that point belongs to or is immediately adjacent to.

        This wil break if cell_size is set to 1, but hey, why would anyone do such a thing?
        """
        cells = set()

        i, j = point

        # upper_left
        cells.add(self.point_hash((i - 1, j - 1)))
        # upper_right
        cells.add(self.point_hash((i - 1, j + 1)))
        # lower_left
        cells.add(self.point_hash((i + 1, j - 1)))
        # lower_rights
        cells.add(self.point_hash((i + 1, j + 1)))

        return cells

    def part_numbers(self) -> list[int]:
        adjacent_point_ids = set()

        for symbol in self.symbols:
            symbol_cells = self.get_cells(symbol["coord"])

            nearby_point_ids = reduce(
                set.union, (self.bucket[symbol_cell] for symbol_cell in symbol_cells)
            )

            adjacent_point_ids.update(
                point_id
                for point_id in nearby_point_ids
                if point_in_bb(symbol["coord"], self.numbers[point_id]["bb"])
            )

        return [self.numbers[id]["val"] for id in adjacent_point_ids]

    def gear_ratios(self) -> list[int]:
        gear_ratios = []

        for symbol in filter(lambda symbol: symbol["val"] == "*", self.symbols):
            symbol_cells = self.get_cells(symbol["coord"])

            nearby_point_ids = reduce(
                set.union, (self.bucket[symbol_cell] for symbol_cell in symbol_cells)
            )

            adjacent_point_ids = tuple(
                point_id
                for point_id in nearby_point_ids
                if point_in_bb(symbol["coord"], self.numbers[point_id]["bb"])
            )

            if len(adjacent_point_ids) == 2:
                gear_ratios.append(
                    self.numbers[adjacent_point_ids[0]]["val"]
                    * self.numbers[adjacent_point_ids[1]]["val"]
                )

        return gear_ratios


def point_in_bb(point: Point, bb: tuple[Point, Point]) -> bool:
    (min_i, min_j), (max_i, max_j) = bb
    i, j = point

    return min_i - 1 <= i <= max_i + 1 and min_j - 1 <= j <= max_j + 1


@stopwatch
def parse(input: TextIOBase) -> Schematic:
    return Schematic(input)


@stopwatch
def part_1(schematic: Schematic):
    return sum(schematic.part_numbers())


@stopwatch
def part_2(schematic: Schematic):
    return sum(schematic.gear_ratios())


if __name__ == "__main__":
    with open("input/day_03.txt", "r") as f:
        data = parse(f)
        print(part_1(data))
        print(part_2(data))
