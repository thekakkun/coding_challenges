class Day13():
    def __init__(self, input):
        self.start_time = int(input.strip().split('\n')[0])
        busses = input.strip().split('\n')[1].split(',')
        self.busses = [int(x) if x.isnumeric() else x for x in busses]
        self.valid_busses = [x for x in self.busses if isinstance(x, int)]

    def earliest_arrival(self):
        time = self.start_time

        while True:
            busses_here = [x for x in self.valid_busses if time % x == 0]
            if busses_here:
                return (time - self.start_time) * busses_here[0]
            else:
                time += 1

    def find_subsequent(self):
        common_gap = self.valid_busses[0]
        time = 0
        gap = 0
        for i in range(len(self.valid_busses) - 1):
            target_bus = self.valid_busses[i]
            next_bus = self.valid_busses[i + 1]
            gap += self.busses[self.busses.index(
                target_bus):self.busses.index(next_bus)].count('x')+1

            while True:
                time += common_gap
                if (time + gap) % next_bus == 0:
                    common_gap *= next_bus
                    break

        return time


test_input_1 = '''939
7,13,x,x,59,x,31,19'''
test_1 = Day13(test_input_1)
print(test_1.earliest_arrival())
print(test_1.find_subsequent())

test_input_2 = '''0
17,x,13,19'''
test_2 = Day13(test_input_2)
print(test_2.find_subsequent())

test_input_3 = '''0
67,7,59,61'''
test_3 = Day13(test_input_3)
print(test_3.find_subsequent())

with open('input/day_13.txt', 'r') as f:
    input = f.read()
    actual = Day13(input)
    print(actual.earliest_arrival())
    print(actual.find_subsequent())
