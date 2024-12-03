import argparse
import importlib

from utils import get_problem


def main(day: int, parts: list[int]):
    with open(f"input/day_{day:02}.txt", "r") as f:
        for part in parts:
            problem = get_problem(day, part)
            problem().run(f)

def get_solver(day: int, part: int):
    module = importlib.import_module(f"solutions.day_{day:02}")
    return getattr(module, f"Part{part}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int)
    parser.add_argument("-p", "--part", type=int, action="append", default=[1, 2])
    args = parser.parse_args()

    day = args.day
    parts = args.part

    main(day, parts)
