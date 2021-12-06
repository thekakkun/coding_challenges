# https://adventofcode.com/2021/day/6

import functools


def count_fish(state):
    return {x: state.count(x) for x in set(state)}


def sim_fish(state, days=80):
    count = count_fish(state)

    rule = {
        0: (8, 6),
        1: (0,),
        2: (1,),
        3: (2,),
        4: (3,),
        5: (4,),
        6: (5,),
        7: (6,),
        8: (7,),
    }

    while 0 < days:
        next_count = {}
        for k, v in count.items():
            for i in rule[k]:
                next_count[i] = next_count.get(i, 0) + v
        count = next_count
        days -= 1

    return sum(count.values())


with open('input/day_06.txt', 'r') as f:
    input = [int(x) for x in f.read().strip().split(',')]
    print(sim_fish(input, 80))
    print(sim_fish(input, 256))
