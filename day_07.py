# https://adventofcode.com/2021/day/7


def dist_1(x, target): return abs(x - target)


def dist_2(x, target): return int(
    abs(x - target) * (abs(x - target) + 1) / 2)


def total_fuel(state, target, dist_f):
    return sum(dist_f(x, target) for x in state)


def align_crabs(state, dist_f):
    target = int(sum(state) / len(state))
    guess = next_guess = total_fuel(state, target, dist_f)

    if (
        total_fuel(state, target, dist_f) <
        total_fuel(state, target+1, dist_f)
    ):
        direction = -1
    else:
        direction = +1

    while True:
        guess = next_guess
        next_guess = total_fuel(state, target + direction, dist_f)
        target += direction
        if guess < next_guess:
            return guess


if __name == '__main__':
    with open('input/day_07.txt', 'r') as f:
        state = tuple(int(x) for x in f.read().split(','))
        print(align_crabs(state, dist_1))
        print(align_crabs(state, dist_2))
