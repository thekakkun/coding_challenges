# https://adventofcode.com/2021/day/10

import functools


def remove_legal_pairs(line):
    pairs = ('()', '[]', '{}', '<>')
    while any((x in line) for x in pairs):
        [line := line.replace(x, '') for x in pairs if x in line]
    return line


def first_illegal(line):
    opener = ('(', '[', '{', '<')
    closer = (')', ']', '}', '>')
    line = remove_legal_pairs(line)
    for i, c in enumerate(line):
        if c in closer:
            for d in line[i-1::-1]:
                if d in opener:
                    return c
    return ''


def get_error_score(input):
    score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}

    return sum(score_table.get(first_illegal(line), 0) for line in input)


def get_completion(line):
    match = {
        '(': ')', '[': ']', '{': '}', '<': '>'
    }

    line = remove_legal_pairs(line)
    if first_illegal(line):
        return ''
    else:
        return ''.join(match[c] for c in line[::-1])


def get_completion_score(input):
    score_table = {
        ')': 1, ']': 2, '}': 3, '>': 4
    }
    input = (x for x in input if not first_illegal(x))

    scores = [
        functools.reduce(
            lambda x, y: x * 5 + score_table[y],
            get_completion(line),
            0
        )
        for line in input
    ]

    return sorted(scores)[(len(scores)-1)//2]


with open('input/day_10.txt', 'r') as f:
    text = f.read().strip().splitlines()
    print(get_error_score(text))
    print(get_completion_score(text))
