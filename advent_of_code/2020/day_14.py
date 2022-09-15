class Day14():
    def __init__(self, input):
        input = input.strip()
        input = input.split('\n')
        self.program = []
        unit = {}
        lines = []
        for line in input:
            if 'mask' in line:
                if unit:
                    unit['lines'] = lines
                    self.program.append(unit)
                    unit = {}
                    lines = []
                unit['mask'] = line.replace('mask = ', '')
            elif 'mem' in line:
                lines.append([int(line.split(' = ')[0].replace('mem[', '').replace(']', '')),
                              int(line.split(' = ')[1])])
        unit['lines'] = lines
        self.program.append(unit)

        self.memory = {}

    def run_program_v1(self):
        for unit in self.program:

            mask = unit['mask']
            lines = unit['lines']
            for line in lines:
                value = get_bin_value(line[1])
                for i, bit in enumerate(mask):
                    if bit == 'X':
                        continue
                    else:
                        value = value[:i] + bit + value[i + 1:]
                self.memory[line[0]] = get_dec_value(value)

    def run_program_v2(self):
        for unit in self.program:
            

            for line in unit['lines']:
                floating_address = get_bin_value(line[0])
                for i, bit in enumerate(unit['mask']):
                    if bit == '0':
                        continue
                    else:
                        floating_address = floating_address[:i] + \
                            bit + floating_address[i + 1:]

                to_write = ['']
                for bit in floating_address:

                    if bit == 'X':
                        to_write *= 2
                        for i in range(len(to_write)):
                            to_write[i] += str(i // (len(to_write) // 2))
                    else:
                        for i in range(len(to_write)):
                            to_write[i] += bit

                for address in to_write:
                    self.memory[get_dec_value(address)] = line[1]


    def get_memory_sum(self):
        return sum(self.memory.values())


def get_bin_value(dec_value):
    bin_value = ''

    while dec_value >= 2:
        bin_value += str(dec_value % 2)
        dec_value = int(dec_value / 2)

    bin_value += str(dec_value)
    return bin_value[::-1].rjust(36, '0')


def get_dec_value(bin_value):
    dec_value = 0

    for i, digit in enumerate(bin_value[::-1]):
        dec_value += int(digit) * 2 ** i

    return dec_value


test_input_1 = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

test_1 = Day14(test_input_1)
test_1.run_program_v1()
print(test_1.get_memory_sum())

test_input_2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

test_2 = Day14(test_input_2)
test_2.run_program_v2()
print(test_2.get_memory_sum())

with open('input/day_14.txt', 'r') as f:
    input = f.read()
    actual = Day14(input)
    actual.run_program_v1()
    print(actual.get_memory_sum())

    actual = Day14(input)
    actual.run_program_v2()
    print(actual.get_memory_sum())
