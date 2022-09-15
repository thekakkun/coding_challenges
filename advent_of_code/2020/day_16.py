import re
from copy import deepcopy
from pprint import pprint


class Day16():
    def __init__(self, input):
        input = input.strip()
        rules, my_ticket, nearby_tickets = input.split('\n\n')

        match_rules = r'(.*): (\d+)-(\d+) or (\d+)-(\d+)'
        self.rules = {x[0]: x[1:] for x in re.findall(match_rules, rules)}

        for k, v in self.rules.items():
            self.rules[k] = list(range(int(v[0]), int(v[1]) + 1)) + \
                list(range(int(v[2]), int(v[3]) + 1))

        match_numbers = r'(\d+)'
        self.my_ticket = [int(x) for x in re.findall(match_numbers, my_ticket)]

        self.nearby_tickets = []
        for nearby_ticket in nearby_tickets.split('\n')[1:]:
            self.nearby_tickets.append(
                [int(x) for x in re.findall(match_numbers, nearby_ticket)])

        self.scan_results = []

    def scan_nearby(self):
        self.scan_results = []
        for ticket in self.nearby_tickets:
            ticket_result = []
            for value in ticket:
                ticket_result.append([value in x for x in self.rules.values()])

            self.scan_results.append(ticket_result)

    def sum_invalid(self):
        sum = 0
        for i, scan_result in enumerate(self.scan_results):
            for j, value_validity in enumerate(scan_result):
                if not any(value_validity):
                    sum += self.nearby_tickets[i][j]

        return sum

    def discard_invalid(self):
        valid_tickets = deepcopy(self.nearby_tickets)
        for i, scan_result in enumerate(self.scan_results):
            for value_validity in scan_result:
                if not any(value_validity):
                    valid_tickets.remove(self.nearby_tickets[i])

        self.nearby_tickets = valid_tickets

    def match_rules(self):
        candidates = [[] for _ in range(len(self.rules))]
        self.fields = [None] * len(self.rules)

        for value in range(len(self.rules)):
            for rule in range(len(self.rules)):
                if all(
                    [self.scan_results[x][value][rule]
                        for x in range(len(self.nearby_tickets))]
                ):
                    candidates[value].append(list(self.rules.keys())[rule])

        while True:
            if not any([bool(x) for x in candidates]):
                break
            for i, candidate in enumerate(candidates):
                if len(candidate) == 1:
                    correct_field = candidate[0]
                    self.fields[i] = correct_field
                    [candidates[x].remove(correct_field)
                     for x in range(len(candidates)) if correct_field in candidates[x]]

    def mult_departure(self):
        result = 1
        for i, field in enumerate(self.fields):
            if 'departure' in field:
                result *= self.my_ticket[i]

        return result


test_input_1 = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

test_1 = Day16(test_input_1)
test_1.scan_nearby()
print(test_1.sum_invalid())
test_1.discard_invalid()

test_input_2 = '''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

test_2 = Day16(test_input_2)
test_2.scan_nearby()
test_2.discard_invalid()
test_2.scan_nearby()
test_2.match_rules()
print(test_2.mult_departure())


with open('input/day_16.txt', 'r') as f:
    input = f.read()
    actual = Day16(input)
    actual.scan_nearby()
    print(actual.sum_invalid())
    actual.discard_invalid()
    actual.scan_nearby()
    actual.match_rules()
    print(actual.mult_departure())
