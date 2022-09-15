# https://adventofcode.com/2021/day/24

from itertools import product


def alu(program, starting_variables=None):
    if starting_variables is None:
        starting_variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    def _f(inp):
        variables = {k: v for k, v in starting_variables.items()}
        instructions = {
            'inp': (lambda _: inp.pop(0)),
            'add': (lambda a, b: a + b),
            'mul': (lambda a, b: a * b),
            'div': (lambda a, b: int(a/b)),
            'mod': (lambda a, b: a % b),
            'eql': (lambda a, b: int(a == b))
        }

        for row in program.strip().splitlines():
            inst, *vals = row.split(' ')
            target = vals[0]

            vals = [variables[val] if val in variables else int(val)
                    for val in vals]
            variables[target] = instructions[inst](*vals)

        return variables

    return _f


def monad(text):
    monads = ['inp' + program for program in text.strip().split('inp')][1::]

    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    monad = alu(text.strip(), variables)

    for i in range(int(1e14-1), 0, -1):
        model = [int(x) for x in str(i)]
        if 0 in model:
            continue
        if monad(model)['z'] == 0:
            return i


def main():
    with open('input/day_24.txt', 'r') as f:
        print(monad(f.read()))


if __name__ == '__main__':
    main()
