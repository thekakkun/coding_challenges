def day_05(input):
    max_id = 0

    for seat in input:
        id = get_id(seat)
        if max_id < id:
            max_id = id

    return max_id


def find_seat(input):
    seat_filled = [0] * day_05(input)
    for seat_code in input:
        seat_filled[get_id(seat_code) - 1] = 1

    for i, seat in enumerate(seat_filled):
        if 0 < i < len(seat_filled):
            if seat == 0:
                if seat_filled[i-1] and seat_filled[i+1]:
                    return i + 1


def get_id(seat):
    row = []
    column = []
    for c in seat[::-1]:
        if c == 'F':
            row.append(0)
        elif c == 'B':
            row.append(2 ** len(row))
        elif c == 'L':
            column.append(0)
        elif c == 'R':
            column.append(2 ** len(column))

    return sum(row) * 8 + sum(column)


test_input = [
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL'
]

print(day_05(test_input))

with open('input/day_05.txt', 'r') as f:
    input = f.read().strip().split('\n')
    print(day_05(input))
    print(find_seat(input))
