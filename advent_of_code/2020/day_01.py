from functools import reduce

def day_01(input, items, target=2020, entries=[]):
    input.sort()
    # print(entries)
    valid_expenses = [x for x in input if
                      x <= target - sum(input[:items-1])]

    if items == 1:
        if target in input:
            entries.append(target)
            return reduce(lambda x, y: x * y, entries)
        else:
            return False
    for i in valid_expenses:
        if day_01(valid_expenses, items-1, target - i, entries + [i]):
            return day_01(valid_expenses, items-1, target - i, entries + [i])
        else:
            continue

test_input = [
    1721,
    979,
    366,
    299,
    675,
    1456
]
print(day_01(test_input, 2))
print(day_01(test_input, 3))

with open('input/day_01.txt', 'r') as f:
    input = [int(x) for x in list(f)]
    print(day_01(input, 2))
    print(day_01(input, 3))
