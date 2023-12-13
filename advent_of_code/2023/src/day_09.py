from io import TextIOBase

from utils import stopwatch


@stopwatch
def parse(input: TextIOBase) -> list[list[int]]:
    data = []

    for line in input:
        data.append([int(n) for n in line.split()])

    return data


@stopwatch
def part_1(data: list[list[int]]):
    return sum(get_nth(seq, len(seq) + 1) for seq in data)


@stopwatch
def part_2(data: list[list[int]]):
    return sum(get_previous(seq) for seq in data)


def get_previous(seq: list[int]) -> int:
    sub_seq = sub_sequences(seq)
    sub_seq_0 = [s[0] for s in sub_seq]

    return sum((-1) ** (i) * n0 for i, n0 in enumerate(sub_seq_0))


def get_nth(seq: list[int], n: int) -> int:
    sub_seq = sub_sequences(seq)
    sub_seq_0 = [s[0] for s in sub_seq]

    return sum(n0 * hyper_triangle_num(i, n - i) for i, n0 in enumerate(sub_seq_0))


def sub_sequences(top_seq: list[int]) -> list[list[int]]:
    result = [top_seq]
    while 2 <= len(result[-1]):
        result.append(
            [result[-1][i + 1] - result[-1][i] for i in range(len(result[-1]) - 1)]
        )

    return result


def hyper_triangle_num(r: int, n: int) -> int:
    return binomial_coefficient(n + (r - 1), r)


def binomial_coefficient(n: int, k: int) -> int:
    if k < 0 or n < k:
        return 0
    if k == 0 or k == n:
        return 1

    k = min(k, n - k)
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)

    return c


if __name__ == "__main__":
    with open("input/day_09.txt", "r") as f:
        sequences = parse(f)
        print(part_1(sequences))
        print(part_2(sequences))
