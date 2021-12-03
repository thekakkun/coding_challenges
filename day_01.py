# https://adventofcode.com/2021/day/1

def sweep_1(report):
    increase_count = 0
    for i in range(1, len(report)):
        if report[i-1] < report[i]:
            increase_count += 1
    return increase_count


def sweep_2(report, window_size=3):
    windowed_report = [sum(report[x-window_size:x])
                       for x in range(window_size, len(report)+1)]
    return sweep_1(windowed_report)


with open('./input/day_01.txt', 'r') as f:
    report = [int(x) for x in f.read().splitlines()]
    print(sweep_1(report))
    print(sweep_2(report))
