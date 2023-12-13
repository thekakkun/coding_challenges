import re
from dataclasses import dataclass
from functools import reduce
from io import TextIOBase
from typing import Iterable, Iterator, TypeVar

from utils import stopwatch


@dataclass
class Node:
    L: str
    R: str


@stopwatch
def parse(input: TextIOBase) -> tuple[str, dict[str, Node]]:
    instructions, network = input.read().split("\n\n")

    nodes = {}

    for line in network.split("\n"):
        m = re.match(r"(?P<node>\w{3}) = \((?P<L>\w{3}), (?P<R>\w{3})\)", line)
        if m:
            m_dict = m.groupdict()
            nodes[m_dict["node"]] = Node(m_dict["L"], m_dict["R"])

    return instructions, nodes


@stopwatch
def part_1(
    instructions: str,
    nodes: dict[str, Node],
    start="AAA",
    goal="ZZZ",
) -> int:
    current_node = start
    steps = 0

    instructions_iter = infinitely_iterate(instructions)

    while current_node != goal:
        _, next_instruction = next(instructions_iter)
        current_node = getattr(nodes[current_node], next_instruction)
        steps += 1

    return steps


@stopwatch
def part_2(
    instructions: str,
    nodes: dict[str, Node],
) -> int:
    loops = [
        loop_lengths(instructions, nodes, node)
        for node in list(nodes)
        if node.endswith("A")
    ]

    return reduce(lcm, loops)


T = TypeVar("T")


def infinitely_iterate(iter: Iterable[T]) -> Iterator[tuple[int, T]]:
    while True:
        for i, x in enumerate(iter):
            yield i, x


def loop_lengths(instructions: str, nodes: dict[str, Node], start: str) -> int:
    visited = set()
    goal_ix = 0

    current_node = start
    for i, (instruction_ix, instruction) in enumerate(infinitely_iterate(instructions)):
        if (instruction_ix, current_node) in visited:
            break

        if current_node.endswith("Z"):
            goal_ix = i

        visited.add((instruction_ix, current_node))
        current_node = getattr(nodes[current_node], instruction)

    return goal_ix


def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a * (b // gcd(a, b))


if __name__ == "__main__":
    with open("input/day_08.txt", "r") as f:
        instructions, network = parse(f)
        print(part_1(instructions, network))
        print(part_2(instructions, network))
