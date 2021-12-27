# https://adventofcode.com/2021/day/21

import re
from itertools import product


def parse_input(text):
    text = text.strip()
    loc = re.findall(r'Player \d+ starting position: (\d+)', text)
    return tuple(int(x) - 1 for x in loc)


def iter_die_deterministic(p):
    roll = p * 3
    while True:
        yield (tuple((roll + i) % 100 + 1 for i in range(3)),)
        roll += 6


def iter_die_dirac():
    while True:
        yield product(range(1, 4), repeat=3)


def get_successors(state, die):
    rolls = next(die)
    successors = {}

    for roll in rolls:
        (position, score, rolls, path_count) = state
        next_position = (position + sum(roll)) % 10
        next_score = score + next_position + 1
        s = (next_position, next_score, rolls+len(roll))

        successors[s] = successors.get(s, 0) + path_count

    return [(*k, v) for k, v in successors.items()]


def simulate(start, rules):
    (die, max_score) = rules

    # {rolls: {score: path_count}}s
    scores = {0: {0: 1}}
    frontier = [(start, 0, 0, 1)]

    while frontier:
        state = frontier.pop(0)
        successors = get_successors(state, die)

        for s in successors:
            (position, score, rolls, path_count) = s
            scores[rolls] = scores.get(rolls, {})
            scores[rolls][score] = scores[rolls].get(score, 0) + path_count

            if max_score <= score:
                continue
            else:
                frontier.append(s)

    return scores


def game_results(scores, rules):
    score_0, score_1 = scores
    (_, max_score) = rules
    results = [0, 0]

    rolls = 3

    while True:
        if any(rolls not in s for s in scores):
            break

        p0_wins = [v for k, v in score_0[rolls].items() if max_score <= k]
        p1_loses = [v for k, v in score_1[rolls-3].items() if k < max_score]
        for c0 in p0_wins:
            for c1 in p1_loses:
                results[0] += c0 * c1

        p0_loses = [v for k, v in score_0[rolls].items() if k < max_score]
        p1_wins = [v for k, v in score_1[rolls].items() if max_score <= k]

        for c0 in p0_loses:
            for c1 in p1_wins:
                results[1] += c0 * c1

        rolls += 3

    return results


if __name__ == '__main__':
    with open('input/day_21.txt', 'r') as f:
        start = parse_input(f.read())

        rules_1 = [(iter_die_deterministic(i), 1000)
                   for i in range(2)]
        (score_1, score_2) = [simulate(start[i], rules_1[i])
                              for i in range(2)]
        winning_roll = max(score_1.keys())
        losing_roll = winning_roll-3
        losing_score = list(score_2[losing_roll].keys())[0]
        print((winning_roll + losing_roll) * losing_score)

        rules_2 = (iter_die_dirac(), 21)
        scores = [simulate(start[i], rules_2) for i in range(2)]
        print(game_results(scores, rules_2))
