from typing import TextIO

from solvers import Solver


class Part1(Solver):
    def _parse(self) -> tuple[list[int], list[int]]:
        lines = [line.split() for line in self.input]
        return map(list, zip(**lines))

    def _solve(self, data):
        return super()._solve(data)
