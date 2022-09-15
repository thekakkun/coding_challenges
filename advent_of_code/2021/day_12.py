# https://adventofcode.com/2021/day/12

def parse_input(text):
    links = [x.split('-') for x in text.strip().splitlines()]
    caves = {}

    for (a, b) in links:
        caves[a] = caves.get(a, set()) | {b}
        caves[b] = caves.get(b, set()) | {a}

    return caves


def successors_1(path, caves):
    return (cave
            for cave in caves[path[-1]]
            if cave not in path or cave.isupper()
            )


def successors_2(path, caves):
    small_cave_count = max(path.count(x) for x in set(path) if x.islower())

    if small_cave_count < 2:
        return (cave
                for cave in caves[path[-1]]
                if cave != 'start')
    else:
        return (cave
                for cave in caves[path[-1]]
                if cave not in path or cave.isupper()
                )


def get_paths(caves, successors, start='start', end='end'):
    paths = set()
    frontier = [[start]]

    while frontier:
        path = frontier.pop()
        s = path[-1]

        for next_path in successors(path, caves):
            path2 = path + [next_path]
            if next_path == end:
                paths.add(tuple(path2))
            else:
                frontier.append(path2)

    return paths


if __name__ == '__main__':
    with open('input/day_12.txt', 'r') as f:
        caves = parse_input(f.read())
        print(len(get_paths(caves, successors_1)))
        print(len(get_paths(caves, successors_2)))
