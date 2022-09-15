from copy import deepcopy
from pprint import pprint


class Day17():
    def __init__(self, input, cycles=6):
        self.cycles = cycles

        input = input.strip()
        plane = input.split('\n')
        plane = [[1 if y == '#' else 0 for y in plane[x]]
                 for x in range(len(plane))]

        self.z_size = cycles * 2 + 1
        self.y_size = cycles * 2 + len(plane)
        self.x_size = cycles * 2 + len(plane[0])

        self.grid = [
            [
                [
                    0 for _ in range(self.x_size)
                ] for _ in range(self.y_size)
            ] for _ in range(self.z_size)
        ]

        for i in range(len(plane)):
            for j in range(len(plane[0])):
                self.grid[cycles][i+cycles][j + cycles] = plane[i][j]

    def run_cycles(self):
        cycle_count = 0
        while cycle_count != self.cycles:
            next_grid = deepcopy(self.grid)
            for z in range(self.z_size):
                for y in range(self.y_size):
                    for x in range(self.x_size):
                        neighbor_count = self.count_neighbors([z, y, x])
                        if self.grid[z][y][x]:
                            if 2 <= neighbor_count[1] <= 3:
                                continue
                            else:
                                next_grid[z][y][x] = 0
                        else:
                            if neighbor_count[1] == 3:
                                next_grid[z][y][x] = 1
            self.grid = next_grid
            cycle_count += 1

    def count_neighbors(self, coordinate):
        neighbor_count = {0: 0, 1: 0}
        z_min, z_max = max(coordinate[0] - 1, 0),\
            min(coordinate[0] + 1, self.z_size-1)
        y_min, y_max = max(coordinate[1] - 1, 0),\
            min(coordinate[1] + 1, self.y_size-1)
        x_min, x_max = max(coordinate[2] - 1, 0),\
            min(coordinate[2] + 1, self.x_size-1)

        for z in range(z_min, z_max+1):
            for y in range(y_min, y_max+1):
                for x in range(x_min, x_max+1):
                    neighbor_count[self.grid[z][y][x]] += 1

        neighbor_count[self.grid[coordinate[0]]
                       [coordinate[1]][coordinate[2]]] -= 1

        return neighbor_count

    def count_active(self):
        count = 0
        for z in self.grid:
            for y in z:
                for x in y:
                    if x:
                        count += 1

        return count


test_input = '''.#.
..#
###'''


test = Day17(test_input)
pprint(test.grid)
test.run_cycles()
print(test.count_active())


with open('input/day_17.txt', 'r') as f:
    input = f.read()
    actual = Day17(input)
    actual.run_cycles
    print(actual.count_active())