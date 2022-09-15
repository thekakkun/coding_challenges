class Day15():
    def __init__(self, input):
        input = input.strip()
        starting_numbers = [int(x) for x in input.split(',')]
        self.history = {x: i for i, x in enumerate(starting_numbers[:-1])}
        self.next_number = starting_numbers[-1]
        self.turn = len(starting_numbers)-1

    def play_game(self, end):
        while True:
            self.history[self.next_number], self.next_number = self.turn,\
                self.turn - self.history.get(self.next_number, self.turn)
            if self.turn + 2 == end:
                break
            else:
                self.turn += 1


test_input_1 = '''0,3,6'''
test_1 = Day15(test_input_1)
test_1.play_game(end=2020)
print(test_1.next_number)
test_1 = Day15(test_input_1)
test_1.play_game(end=30000000)
print(test_1.next_number)

input = '''2,0,1,9,5,19'''
actual = Day15(input)
actual.play_game(end=2020)
print(actual.next_number)
actual = Day15(input)
actual.play_game(end=30000000)
print(actual.next_number)
