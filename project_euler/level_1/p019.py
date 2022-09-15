import time
from functools import reduce

start_time = time.time()


def p019(start, end):
    """Counting Sundays

    Problem 19

    You are given the following information, but you may prefer to do some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.

        A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """

    calendar = [
        [[1, 1, 1900], 2]
    ]

    while True:
        next_day = get_next_day(calendar[-1][0])
        calendar.append([next_day, calendar[-1][1] % 7 + 1])

        if next_day == end:
            break

    relevant_range = calendar[[x[0] for x in calendar].index(start):]
    first_sundays = [x for x in relevant_range if x[0][0] == 1 and x[1] == 1]

    return len(first_sundays)


def days_in_month(year):
    normal_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    leap_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if year % 4 != 0:
        return normal_year
    elif year % 400 == 0:
        return normal_year
    else:
        return leap_year


def get_next_day(date):
    day = date[0]
    month = date[1]
    year = date[2]

    next_day = [None, None, None]

    days_list = days_in_month(year)

    if days_list[month] == day:
        next_day[0] = 1
        next_day[1] = month % 12 + 1
        if day == 31 and month == 12:
            next_day[2] = year + 1
        else:
            next_day[2] = year
    else:
        next_day[0] = day + 1
        next_day[1] = month
        next_day[2] = year

    return next_day


print(p019(start=[1, 1, 1901], end=[31, 12, 2000]))
print('Completed in', time.time() - start_time, 'seconds')
