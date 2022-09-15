import csv
import os
import time

start_time = time.time()


def p022(name_list):
    """Names scores

    Problem 22

    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """

    score_sum = 0
    name_list.sort()

    for i, name in enumerate(name_list):
        score_sum += alpha_value(name) * (i + 1)

    return score_sum


def alpha_value(name):
    value = 0
    values = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    for letter in name.lower():
        value += values[letter]

    return value


with open(os.path.join('level_1', 'p022_names.txt'), 'r', newline='', ) as f:
    name_list = list(csv.reader(f))[0]
    print(p022(name_list))
    print('Completed in', time.time() - start_time, 'seconds')
