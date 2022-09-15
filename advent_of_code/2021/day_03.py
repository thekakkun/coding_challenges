# https://adventofcode.com/2021/day/3

def get_gamma(report):
    threshold = len(report) / 2
    data_len = len(report[0])
    report = [int(x, 2) for x in report]
    gamma = ''

    while sum(report):
        count = sum([x % 2 for x in report])
        if threshold <= count:
            gamma = '1' + gamma
        else:
            gamma = '0' + gamma

        report = [int(x/2) for x in report]

    return gamma.zfill(data_len)


def get_rating(report, value):
    criteria = {
        'o': lambda x: x[i] == gamma[i],
        'co2': lambda x: x[i] != gamma[i],
    }

    for i in range(len(report[0])):
        gamma = get_gamma(report)
        report = [x for x in report if criteria[value](x)]
        if len(report) == 1:
            return report[0]


def diag_1(report):
    gamma = get_gamma(report)
    epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])

    return int(gamma, 2) * int(epsilon, 2)


def diag_2(report):
    o = get_rating(report, 'o')
    co2 = get_rating(report, 'co2')

    return int(o, 2) * int(co2, 2)


if __name__ == '__main__':
    with open('input/day_03.txt', 'r') as f:
        report = f.read().splitlines()
        print(diag_1(report))
        print(diag_2(report))
