from copy import deepcopy


class Day11:
    def __init__(self, input):
        layout = input.strip()
        layout = layout.split('\n')
        self.row_count, self.col_count = len(layout), len(layout[0])
        self.layout = [[0] * self.col_count for _ in range(self.row_count)]
        for row in range(self.row_count):
            for col in range(self.col_count):
                if layout[row][col] == '.':
                    self.layout[row][col] = -1
                elif layout[row][col] == 'L':
                    self.layout[row][col] = 0
                elif layout[row][col] == '#':
                    self.layout[row][col] = 1

    def part_1(self):
        while True:
            self.update_seats(look_far=False)
            if self.previous_layout == self.layout:
                break

        return self.count_occupied()

    def part_2(self):
        while True:
            self.update_seats(look_far=True)
            if self.previous_layout == self.layout:
                break

        return self.count_occupied()

    def look_close(self, seat):
        surrounding_seats = {
            -1: 0,
            0: 0,
            1: 0
        }
        top, bottom = max(0, seat[0]-1), min(self.row_count-1, seat[0] + 1)
        left, right = max(0, seat[1]-1), min(self.col_count-1, seat[1] + 1)

        for row in range(top, bottom+1):
            for col in range(left, right+1):
                if [row, col] != seat:
                    surrounding_seats[self.layout[row][col]] += 1

        return surrounding_seats

    def look_far(self, seat):
        visible_seats = []
        directions = [[-1, -1], [-1, 0], [-1, 1],
                      [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        for direction in directions:
            checking = seat.copy()
            while True:
                checking = [sum(x) for x in zip(checking, direction)]

                if not all([0 <= checking[0] <= self.row_count-1, 0 <= checking[1] <= self.col_count-1]):
                    visible_seats.append(-1)
                    break
                if self.layout[checking[0]][checking[1]] == -1:
                    continue
                elif self.layout[checking[0]][checking[1]] == 0:
                    visible_seats.append(0)
                    break
                elif self.layout[checking[0]][checking[1]] == 1:
                    visible_seats.append(1)
                    break

        visible_status = {
            -1: 0,
            0: 0,
            1: 0
        }
        for i in visible_seats:
            visible_status[i] += 1

        return visible_status

    def update_seats(self, look_far):
        if look_far:
            filled_threshold = 5
            checking_func = self.look_far
        else:
            filled_threshold = 4
            checking_func = self.look_close

        updated_layout = deepcopy(self.layout)

        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.layout[row][col] == 0:
                    if checking_func([row, col])[1] == 0:
                        updated_layout[row][col] = 1
                elif self.layout[row][col] == 1:
                    if checking_func([row, col])[1] >= filled_threshold:
                        updated_layout[row][col] = 0

        self.previous_layout = self.layout
        self.layout = updated_layout

    def count_occupied(self):
        count = 0
        for row in self.layout:
            for col in row:
                if col == 1:
                    count += 1

        return count


test_input = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

test = Day11(test_input)
print(test.part_1())
test = Day11(test_input)
print(test.part_2())

with open('input/day_11.txt', 'r') as f:
    input = f.read().strip()
    actual = Day11(input)
    print(actual.part_1())
    actual = Day11(input)
    print(actual.part_2())
