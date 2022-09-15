import re


def day_07(input, target='shiny gold'):
    bag_count = 0
    rules = parse_input(input)

    for bag in rules.keys():
        if contains_target(rules, bag):
            bag_count += 1

    return bag_count


def day_07_updated(input, top_bag='shiny gold'):
    rules = parse_input(input)
    if not rules[top_bag]:
        return 0
    else:
        return sum([count * (day_07_updated(input, top_bag=bag) + 1) for (bag, count) in rules[top_bag].items()])


def contains_target(input, bag, target='shiny gold'):
    if not input[bag]:
        return False
    elif target in input[bag]:
        return True
    else:
        return any([contains_target(input, x) for x in input[bag].keys()])


def parse_input(input):
    rules_list = input.replace('bags', 'bag').replace('.', '').split('\n')
    rules_list = [x.split(' contain ') for x in rules_list]
    rules_list = [[x[0], x[1].split(', ')] for x in rules_list]

    rules = {}
    for rule in rules_list:
        parent_bag = rule[0].replace(' bag', '')
        rules[parent_bag] = {}
        for contents in rule[1]:
            m = re.match(r'(?P<count>\d) (?P<bag_type>.*) bag', contents)
            if m:
                rules[parent_bag][m['bag_type']] = int(m['count'])

    return rules


test_input = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

test_input_updated = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

print(day_07(test_input))
print(day_07_updated(test_input))
print(day_07_updated(test_input_updated))

with open('input/day_07.txt', 'r') as f:
    input = f.read().strip()
    print(day_07(input))
    print(day_07_updated(input))
