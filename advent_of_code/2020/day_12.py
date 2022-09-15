from math import cos, sin, radians


class Day12():
    def __init__(self, input, target):
        instructions = input.strip()
        self.instructions = [[x[0], int(x[1:])]
                             for x in instructions.split('\n')]
        self.direction = [1, 0]
        self.location = [0, 0]
        self.waypoint = [10, 1]
        self.target = target

    def run_instructions(self):
        for instruction in self.instructions:
            self.move(instruction)

    def move(self, instruction):
        movement = [0, 0]
        if instruction[0] == 'N':
            movement = [0, instruction[1]]
        elif instruction[0] == 'S':
            movement = [0, -instruction[1]]
        elif instruction[0] == 'E':
            movement = [instruction[1], 0]
        elif instruction[0] == 'W':
            movement = [-instruction[1], 0]
        elif instruction[0] == 'L':
            self.rotate(instruction)
        elif instruction[0] == 'R':
            self.rotate(instruction)
        elif instruction[0] == 'F':
            if self.target == 'ship':
                movement = [x * instruction[1] for x in self.direction]
            elif self.target == 'waypoint':
                movement = [x * instruction[1] for x in self.waypoint]
                self.location = [sum(x) for x in zip(self.location, movement)]
                movement = [0, 0]

        if self.target == 'ship':
            self.location = [sum(x) for x in zip(self.location, movement)]
        if self.target == 'waypoint':
            self.waypoint = [sum(x) for x in zip(self.waypoint, movement)]

        print(instruction)
        print(self.location, self.waypoint, self.direction)

        # print(instruction, self.direction, self.waypoint, self.location)

    # def move_ship(self, instruction):
    #     movement = [0, 0]
    #     if instruction[0] == 'N':
    #         movement = [0, instruction[1]]
    #     elif instruction[0] == 'S':
    #         movement = [0, -instruction[1]]
    #     elif instruction[0] == 'E':
    #         movement = [instruction[1], 0]
    #     elif instruction[0] == 'W':
    #         movement = [-instruction[1], 0]
    #     elif instruction[0] == 'L':
    #         self.rotate(instruction)
    #     elif instruction[0] == 'R':
    #         self.rotate(instruction)
    #     elif instruction[0] == 'F':
    #         movement = [x * instruction[1] for x in self.direction]

    #     self.location = [sum(x) for x in zip(self.location, movement)]
    #     print(instruction, self.direction, self.location)

    # def move_waypoint(self, instruction):
    #     movement = [0, 0]
    #     if instruction[0] == 'N':
    #         movement = [0, instruction[1]]
    #     elif instruction[0] == 'S':
    #         movement = [0, -instruction[1]]
    #     elif instruction[0] == 'E':
    #         movement = [instruction[1], 0]
    #     elif instruction[0] == 'W':
    #         movement = [-instruction[1], 0]
    #     elif instruction[0] == 'L':
    #         self.rotate(instruction)
    #     elif instruction[0] == 'R':
    #         self.rotate(instruction)
    #     elif instruction[0] == 'F':
    #         movement = [x * instruction[1] for x in self.direction]

    def get_distance(self):
        return sum([abs(x) for x in self.location])

    def rotate(self, instruction):
        if self.target == 'ship':
            target_direction = self.direction
        elif self.target == 'waypoint':
            target_direction = self.waypoint

        if instruction[0] == 'R':
            rotated = [
                target_direction[0] * cos(radians(instruction[1]))
                + target_direction[1] * sin(radians(instruction[1])),
                target_direction[0] * -sin(radians(instruction[1]))
                + target_direction[1] * cos(radians(instruction[1]))
            ]
        else:
            rotated = [
                target_direction[0] * cos(radians(instruction[1]))
                + target_direction[1] * -sin(radians(instruction[1])),
                target_direction[0] * sin(radians(instruction[1]))
                + target_direction[1] * cos(radians(instruction[1]))
            ]

        if self.target == 'ship':
            self.direction = [round(x) for x in rotated]
        elif self.target == 'waypoint':
            self.waypoint = [round(x) for x in rotated]


test_input = '''F10
N3
F7
R90
F11'''

test_part_1 = Day12(test_input, 'ship')
test_part_1.run_instructions()
print(test_part_1.get_distance())
test_part_2 = Day12(test_input, 'waypoint')
test_part_2.run_instructions()
print(test_part_2.get_distance())

with open('input/day_12.txt', 'r') as f:
    input = f.read()
    actual_part_1 = Day12(input, 'ship')
    actual_part_1.run_instructions()
    print(actual_part_1.get_distance())
    actual_part_2 = Day12(input, 'waypoint')
    actual_part_2.run_instructions()
    print(actual_part_2.get_distance())
