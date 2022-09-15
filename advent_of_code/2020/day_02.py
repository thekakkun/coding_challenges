from functools import reduce


def day_02(input):
    valid_count = 0
    for entry in input:
        min_count, max_count, char, password = parse_policy(entry)
        char_count = sum([1 for x in password if x == char])
        if min_count <= char_count <= max_count:
            valid_count += 1

    return valid_count


def day_02_updated(input):
    valid_count = 0
    for entry in input:
        min_count, max_count, char, password = parse_policy(entry)
        check = [password[min_count-1] == char, password[max_count-1] == char]
        if any(check) and not all(check):
            valid_count += 1

    return valid_count


def parse_policy(entry):
    count_rule, char, password = entry.split()
    min_count, max_count = [int(x) for x in count_rule.split('-')]
    char = char.replace(':', '')
    return (min_count, max_count, char, password)


test_input = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

print(day_02(test_input))
print(day_02_updated(test_input))

with open('input/day_02.txt', 'r') as f:
    input = list(f)
    print(day_02(input))
    print(day_02_updated(input))
