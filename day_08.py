# https://adventofcode.com/2021/day/8

def parse_input(text):
    return (
        tuple(
            tuple(
                frozenset(z) for z in y.split()
            )
            for y in x.split(' | ')
        )
        for x in text.splitlines()
    )


def count_unique(disp_data):
    return sum(1
               for x in disp_data
               for y in x[1]
               if len(y) in (2, 3, 4, 7)
               )


def decode(entry):
    true_segments = {
        0: set('abcefg'),
        1: set('cf'),
        2: set('acdeg'),
        3: set('acdfg'),
        4: set('bcdf'),
        5: set('abdfg'),
        6: set('abdefg'),
        7: set('acf'),
        8: set('abcdefg'),
        9: set('abcdfg')
    }

    seg_diff = {
        sum(len(true_segments[i] - v) for _, v in true_segments.items()): i
        for i in range(10)
    }

    (signal_pattern, output) = entry
    digit_dict = {}
    for digit in signal_pattern:
        digit_dict[digit] = seg_diff[sum(
            len(digit - x) for x in signal_pattern)]

    return sum(digit_dict[x] * 10**i for i, x in enumerate(output[::-1]))


def count_sums(input):
    return sum(decode(x) for x in input)


if __name__ == '__main__':
    with open('input/day_08.txt', 'r') as f:
        text = parse_input(f.read().strip())
        print(count_unique(text))
        print(count_sums(text))
