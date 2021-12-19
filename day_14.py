# https://adventofcode.com/2021/day/14

def parse_input(text):
    (template, rules) = text.strip().split('\n\n')

    rules = {
        rule[:2]: rule[-1]
        for rule in rules.splitlines()
    }

    return template, rules


def apply_process(polymer, rules, steps=10):
    # Too slow for anything over 15-ish steps
    while steps:
        polymer = ''.join(
            (
                el + rules[polymer[i:i+2]]
                if (i < len(polymer) - 1)
                else el
            )
            for i, el in enumerate(polymer)
        )
        steps -= 1

    return polymer


def count_elements(polymer, rules, steps=0):
    pair_count = {}
    for i, el in enumerate(polymer):
        if len(polymer) < i + 2:
            break
        pair = polymer[i:i+2]
        pair_count[pair] = pair_count.get(pair, 0) + 1

    while steps:
        last_pair_count, pair_count = pair_count, {}
        for pair, count in last_pair_count.items():
            results = (
                pair[0] + rules[pair],
                rules[pair] + pair[1]
            )
            for result in results:
                pair_count[result] = pair_count.get(result, 0) + count
        steps -= 1

    el_count = {}
    for k, v in pair_count.items():
        for el in k:
            el_count[el] = el_count.get(el, 0) + v
    el_count[polymer[0]] += 1
    el_count[polymer[-1]] += 1

    return {k: v//2 for k, v in el_count.items()}


if __name == '__main__':
    with open('input/day_14.txt', 'r') as f:
        (template, rules) = parse_input(f.read())

        el_count_1 = count_elements(template, rules, steps=10)
        print(max(el_count_1.values()) - min(el_count_1.values()))

        el_count_2 = count_elements(template, rules, steps=40)
        print(max(el_count_2.values()) - min(el_count_2.values()))
