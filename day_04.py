# https://adventofcode.com/2021/day/4

import math


def parse_bingo(input):
    numbers, boards = input.strip().split('\n', maxsplit=1)

    numbers = (int(x) for x in numbers.split(','))
    boards = list(
        list(int(y) for y in x.replace('\n', ' ').split()) for x in boards.strip().split('\n\n')
    )

    return (numbers, boards)


def is_bingo(board):
    board_size = int(math.sqrt(len(board)))
    bingo_match = [-1] * board_size

    if board.count(-1) < board_size:
        return False
    else:
        return (
            bingo_match in (board[i::board_size] for i in range(board_size))
            or
            bingo_match in (
                board[i*board_size:(i+1)*board_size] for i in range(board_size))
        )


def play_bingo_1(game):
    (numbers, boards) = game

    for n in numbers:
        for i, board in enumerate(boards):
            boards[i] = [-1 if x == n else x for x in board]
            if is_bingo(boards[i]):
                return n * sum(x for x in boards[i] if x != -1)


def play_bingo_2(game):
    (numbers, boards) = game
    remainder = len(boards)

    for n in numbers:
        for i, board in enumerate(boards):
            if is_bingo(board):
                continue
            else:
                boards[i] = [-1 if x == n else x for x in board]
                if is_bingo(boards[i]):
                    if remainder == 1:
                        return n * sum(x for x in boards[i] if x != -1)
                    else:
                        remainder -= 1


with open('input/day_04.txt', 'r') as f:
    input = f.read().strip()
    print(play_bingo_1(parse_bingo(input)))
    print(play_bingo_2(parse_bingo(input)))
