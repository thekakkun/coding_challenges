from abc import ABC, abstractmethod

import utils
import time


class Solver[T, U](ABC):
    def __init__(self, input: str):
        self.input = input

    def run(self) -> U:
        start_time = time.perf_counter()

        data = self._parse(self.input)
        parse_time = time.perf_counter()
        print(f"parsed input in {utils.format_seconds(parse_time - start_time)}")

        solution = self._solve(data)
        solve_time = time.perf_counter()
        print(f"parsed input in {utils.format_seconds(solve_time  -parse_time)}")

        print(f"Answer: {solution}")

        return solution

    @abstractmethod
    def _parse(self) -> T: ...

    @abstractmethod
    def _solve(self, data: T) -> U: ...
