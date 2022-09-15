def day_03(input, location=[0, 0], slope=[1, 3]):
    tree_map = parse_map(input)
    tree_count = 0
    slope_size = [len(tree_map), len(tree_map[0])]

    while True:
        if tree_map[location[0]][location[1]]:
            tree_count += 1
        location = [
            location[0] + slope[0],
            (location[1] + slope[1]) % slope_size[1]]
        if location[0] >= slope_size[0]:
            break
    return tree_count


def test_multiple_slopes(input, slope_choices):
    product = 1
    for choice in slope_choices:
        product *= day_03(input, slope=choice)

    return product


def parse_map(input):
    input = input.replace('.', '0').replace('#', '1')
    tree_map = input.split('\n')
    return [[int(y) for y in x] for x in tree_map if x]


test_input = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

possible_slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

print(day_03(test_input))
print(test_multiple_slopes(test_input, possible_slopes))

with open('input/day_03.txt', 'r') as f:
    input = f.read()
    print(day_03(input))
    print(test_multiple_slopes(input, possible_slopes))
