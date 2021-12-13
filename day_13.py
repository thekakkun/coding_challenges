# https://adventofcode.com/2021/day/13

def parse_input(input):
    (dots, folds) = input.strip().split('\n\n')

    dots = set(
        tuple(int(x) for x in line.split(','))
        for line in dots.splitlines()
    )
    folds = tuple(
        (axis, int(along))
        for axis, along in [
            line.replace('fold along ', '').split('=')
            for line in folds.splitlines()
        ]
    )

    return (dots, folds)


def make_fold(dots, fold):
    (axis, along) = fold
    result = set()

    for dot in dots:
        (x, y) = dot
        if axis == 'x' and along < x:
            dot = (along * 2 - x, y)
        elif axis == 'y' and along < y:
            dot = (x, along * 2 - y)
        result.add(dot)
    return result


def get_code(dots, folds):
    for fold in folds:
        dots = make_fold(dots, fold)
    return dots


def print_code(dots):
    (y_size, x_size) = tuple(max(x) for x in zip(*dots))
    grid = tuple(
        ''.join(
            '#' if (y, x) in dots else ' '
            for y in range(y_size+1)
        )
        for x in range(x_size+1)
    )

    for line in grid:
        print(line)


with open('input/day_13.txt', 'r') as f:
    (dots, folds) = parse_input(f.read())
    print(len(make_fold(dots, folds[0])))
    print_code(get_code(dots, folds))
