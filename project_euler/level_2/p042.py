import csv
import math
import os
import time

start_time = time.time()


def p042(word_list):
    """Coded triangle numbers

    Problem 42

    The nth term of the sequence of triangle numbers is given by, t_n = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a triangle number then we shall call the word a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
    """

    triangle_word_count = 0

    for word in word_list:
        if is_triangle_number(get_word_value(word)):
            print(word, get_word_value(word))
            triangle_word_count += 1

    return triangle_word_count


def get_word_value(word):
    word = word.lower()
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

    return sum([values[x] for x in word])


def is_triangle_number(n):
    if math.floor(math.sqrt(2 * n)) * (math.floor(math.sqrt(2 * n)) + 1) == 2 * n:
        return True
    else:
        return False


with open(os.path.join('level_2', 'p042_words.txt'), 'r', newline='') as f:
    word_list = list(csv.reader(f))[0]
    print(p042(word_list))

print('Completed in', time.time() - start_time, 'seconds')
