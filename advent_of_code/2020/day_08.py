from copy import deepcopy


def day_08(input):
    acc = 0
    loc = 0
    ran = []
    jmp_nop = []

    if isinstance(input, str):
        instructions = parse_input(input)
    else:
        instructions = input

    while loc not in ran:
        ran.append(loc)
        operation, argument = instructions[loc]

        if operation == 'acc':
            acc += argument
            loc += 1
        elif operation == 'jmp':
            jmp_nop.append(loc)
            loc += argument
        elif operation == 'nop':
            jmp_nop.append(loc)
            loc += 1

        if loc == len(instructions):
            return (loc, acc, jmp_nop)

    return (loc, acc, jmp_nop)


def day_08_updated(input):
    instructions = parse_input(input)

    corruption_candidates = day_08(input)[2]
    for candidate in corruption_candidates:
        updated_instructions = deepcopy(instructions)
        if instructions[candidate][0] == 'jmp':
            updated_instructions[candidate][0] = 'nop'
        elif instructions[candidate][0] == 'nop':
            updated_instructions[candidate][0] = 'jmp'

        results = day_08(updated_instructions)

        if results[0] == len(instructions):
            return results[1]


def parse_input(input):
    return [[x.split(' ')[0], int(x.split(' ')[1])] for x in input.strip().split('\n')]


test_input = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

print(day_08(test_input)[1])
print(day_08_updated(test_input))


with open('input/day_08.txt') as f:
    input = f.read()
    print(day_08(input)[1])
    print(day_08_updated(input))
