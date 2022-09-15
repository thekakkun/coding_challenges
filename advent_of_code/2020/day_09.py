def day_09(input, preamble_len):
    numbers = [int(x) for x in input.strip().split('\n')]
    for i in range(preamble_len+1, len(numbers)):
        preamble = numbers[i-preamble_len-1:i-1]

        for j in preamble:
            if numbers[i-1] - j in preamble:
                break
        else:
            return numbers[i-1]


def day_09_updated(input, preamble_len):
    exploit = day_09(input, preamble_len)
    numbers = [int(x) for x in input.strip().split('\n')]
    sum_count = 2
    num_set = []

    while True:
        for i in range(len(numbers)-1):
            num_set = numbers[i:i+sum_count]
            if sum(num_set) == exploit:
                return min(num_set) + max(num_set)
        sum_count += 1


test_input = '''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''
preamble = 5

print(day_09(test_input, preamble))
print(day_09_updated(test_input, preamble))

with open('input/day_09.txt', 'r') as f:
    input = f.read()
    print(day_09(input, 25))
    print(day_09_updated(input, 25))
