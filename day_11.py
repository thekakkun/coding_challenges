# https://adventofcode.com/2021/day/11

def parse_input(text):
    octos = [
        [int(octo) for octo in row]
        for row in text.splitlines()
    ]

    c = len(octos[0])
    octos.insert(0, [-1 for _ in range(c)])
    octos.append([-1 for _ in range(c)])

    octos = [
        [-1, *row, -1] for row in octos
    ]

    return octos


def get_flashes(octos):
    return set(
        (i, j)
        for i, row in enumerate(octos)
        for j, octo in enumerate(row)
        if octo == 0
    )


def run_step(octos):
    octos = [
        [
            (octo + 1) % 10 if 0 <= octo else octo
            for octo in row
        ]
        for row in octos
    ]

    flashes = get_flashes(octos)
    flashed = set()

    while flashes:
        flash = flashes.pop()

        if flash in flashed:
            continue

        flashed.add(flash)
        (flash_i, flash_j) = flash
        flash_range = zip(
            range(flash_i-1, flash_i+2),
            range(flash_j-1, flash_j+2)
        )

        for i in range(flash_i-1, flash_i+2):
            for j in range(flash_j-1, flash_j+2):
                if 0 < octos[i][j]:
                    octos[i][j] = (octos[i][j]+1) % 10
        flashes = get_flashes(octos) - flashed

    return (len(flashed), octos)


def count_flashes(octos, steps):
    flash_count = 0
    while steps:
        (flashes, octos) = run_step(octos)
        flash_count += flashes
        steps -= 1
    return flash_count


def find_simul(octos):
    steps = 0
    while sum(
        1
        for row in octos
        for octo in row
        if 0 < octo
    ):
        (_, octos) = run_step(octos)
        steps += 1

    return steps


if __name__ == '__main__':
    with open('input/day_11.txt', 'r') as f:
        octos = parse_input(f.read().strip())
        print(count_flashes(octos, 100))
        print(find_simul(octos))
