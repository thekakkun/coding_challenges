from functools import reduce


def day_10(adapters):
    gaps = [0] * 3

    for i in range(len(adapters) - 1):
        difference = adapters[i+1] - adapters[i]
        gaps[difference - 1] += 1

    return gaps[0] * gaps[2]


def day_10_updated(adapters):
    gaps = []
    for i in range(1, len(adapters)):
        gaps.append(adapters[i] - adapters[i-1])

    one_chains = []
    count = 0
    for gap in gaps:
        if gap == 3:
            if count >= 2:
                one_chains.append(count)
            count = 0
        if gap == 1:
            count += 1
    combinations = []
    for chain in one_chains:
        combinations.append(count_arrangements(get_test_adaptors(chain)))

    return reduce(lambda x, y: x * y, combinations)


def get_test_adaptors(chain_length):
    adaptors = [0]
    for i in range(chain_length+1):
        adaptors.append(i + 3)
    adaptors.append(max(adaptors) + 3)

    return adaptors

def count_arrangements(adapters, remove_from=0, count=0):
    count = 0
    input, output = min(adapters), max(adapters)
    for i in range(remove_from, len(adapters)):
        test_arrangement = adapters.copy()
        del test_arrangement[i]
        if device_charges(test_arrangement, input, output):
            count += count_arrangements(test_arrangement,
                                    remove_from=i, count=count)

    return count + 1


def get_adapters(input, outlet=0, built_in=3):
    adapters = [int(x) for x in input.strip().split('\n')]
    adapters.append(outlet)
    adapters.append(max(adapters) + built_in)
    adapters.sort()

    return adapters


def device_charges(adapters, input, output):
    if input not in adapters or output not in adapters:
        return False
    for i in range(len(adapters) - 1):
        if adapters[i+1] - adapters[i] > 3:
            return False
    return True


test_input_1 = '''16
10
15
5
1
11
7
19
6
12
4'''

test_input_2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

print(day_10(get_adapters(test_input_1)))
print(day_10_updated(get_adapters(test_input_1)))
print(day_10(get_adapters(test_input_2)))
print(day_10_updated(get_adapters(test_input_2)))

with open('input/day_10.txt', 'r') as f:
    input = f.read()
    print(day_10(get_adapters(input)))
    print(day_10_updated(get_adapters(input)))
