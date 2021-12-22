# https://adventofcode.com/2021/day/20


def parse_input(text):
    algo, img = text.strip().split('\n\n')

    algo = tuple(1 if c == '#' else 0 for c in algo)
    img = tuple(
        tuple(1 if c == '#' else 0 for c in line)
        for line in img.splitlines()
    )

    return algo, img


def get_algo_loc(img, pixel, bg='0'):
    surroundings = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    )
    rows, cols = len(img), len(img[0])

    loc = ''
    for direction in surroundings:
        (p_r, p_c) = (sum(x) for x in zip(pixel, direction, (-1, -1)))
        if p_r in range(rows) and p_c in range(cols):
            loc += str(img[p_r][p_c])
        else:
            loc += bg

    return int(loc, 2)


def enhance(algo, img, times):
    for i in range(times):
        previous_img = tuple(row[:] for row in img)
        rows, cols = len(previous_img), len(previous_img[0])
        next_rows, next_cols = rows+2, cols+2

        if algo[0] == 0:
            bg = '0'
        else:
            bg = str(i % 2)

        img = tuple(
            tuple(algo[get_algo_loc(previous_img, (r, c), bg)]
                  for c in range(next_cols))
            for r in range(next_rows)
        )

    return img


def count_lights(img):
    return sum(sum(r) for r in img)


if __name__ == '__main__':
    with open('input/day_20.txt', 'r') as f:
        algo, img = parse_input(f.read())

        img_2 = enhance(algo, img, 2)
        print(count_lights(img_2))

        img_50 = enhance(algo, img, 50)
        print(count_lights(img_50))
