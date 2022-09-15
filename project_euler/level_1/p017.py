import time

start_time = time.time()


def p017(n):
    """Number letter counts

    Problem 17

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
    """

    special_names = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    units = {
        100: 'hundred',
        1000: 'thousand'
    }
    written_number = {}

    for i in range(1, n + 1):
        written_number[i] = ''

        current_number = i
        if current_number == 0:
            continue

        while [x for x in units.keys() if x <= current_number]:
            unit = max([x for x in units.keys() if x <= current_number])
            digit = current_number // unit

            written_number[i] += (special_names[digit] + units[unit])
            current_number -= digit * unit

            if unit == 100 and current_number != 0:
                written_number[i] += 'and'

        specials_list = [x for x in special_names.keys() if x <=
                         current_number]

        while specials_list:
            written_number[i] += special_names[max(specials_list
                                                   )]

            current_number -= max(specials_list
                                  )
            specials_list = [
                x for x in special_names.keys() if x <= current_number]

    return sum([len(written_number[x]) for x in written_number.keys()])


print(p017(5))
print(p017(1000))
print('Completed in', time.time() - start_time, 'seconds')
