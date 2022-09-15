def day_06(input):
    count_sum = 0
    groups = parse_input(input)

    for group in groups:
        count_sum += len(count_responses(group))

    return count_sum


def day_06_updated(input):
    count_sum = 0
    groups = parse_input(input)
    for group in groups:
        responses = count_responses(group)
        count_sum += sum([1 for x in responses.values() if len(group) == x])

    return count_sum


def count_responses(group):
    yes_count = {}
    for person in group:
        for answer in person:
            answer_count = yes_count.get(answer, 0) + 1
            yes_count[answer] = answer_count

    return yes_count


def parse_input(input):
    input = [x.split('\n') for x in input.split('\n\n')]
    return input


test_input = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

print(day_06(test_input))
print(day_06_updated(test_input))

with open('input\day_06.txt', 'r') as f:
    input = f.read().strip()
    print(day_06(input))
    print(day_06_updated(input))
