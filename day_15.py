# https://adventofcode.com/2021/day/15

import math


def parse_input(input):
    return tuple(
        tuple(int(x) for x in row)
        for row in input.strip().splitlines()
    )


def expand_map(risk_map, times=5):
    rows, cols = len(risk_map), len(risk_map[0])
    return tuple(
        tuple(
            (risk_map[r % rows][c % cols] + r // rows + c // cols - 1) % 9 + 1
            for c in range(cols * times)
        )
        for r in range(rows * times)
    )


def dijkstra(risk_map, start=(0, 0), goal=None):
    rows, cols = len(risk_map), len(risk_map[0])
    max_dist = 10 * rows * cols
    if goal is None:
        goal = (rows-1, cols-1)

    Q = set()
    dist = {}

    for vertex in ((r, c) for r in range(rows) for c in range(cols)):
        Q.add(vertex)
        dist[vertex] = math.inf

    dist[start] = 0

    while Q:
        u = sorted(Q, key=dist.get)[0]
        if u == goal:
            break

        Q.remove(u)

        neighbors = (
            (r, c)
            for i, r in enumerate(range(u[0]-1, u[0]+2))
            for j, c in enumerate(range(u[1]-1, u[1]+2))
            if (i + j) % 2 == 1
            if r in range(rows)
            if c in range(cols)
        )

        for v in neighbors:
            if v not in Q:
                continue
            v_r, v_c = v
            alt = dist.get(u, max_dist) + risk_map[v_r][v_c]

            if alt < dist.get(v, max_dist):
                dist[v] = alt

    return dist


def manhattan(v_1, v_2):
    return sum(abs(r - c) for r, c in zip(v_1, v_2))


def a_star(risk_map, cost, start=(0, 0), goal=None):
    rows, cols = len(risk_map), len(risk_map[0])
    if goal is None:
        goal = (rows - 1, cols - 1)

    Q = set()
    dist = {}
    heuristic = {}

    for vertex in ((r, c) for r in range(rows) for c in range(cols)):
        dist[vertex] = math.inf
        heuristic[vertex] = math.inf

    Q.add(start)
    dist[start] = 0
    heuristic[start] = cost(start, goal)

    count = 0
    while Q:
        u = sorted(Q, key=heuristic.get)[0]
        if u == goal:
            return dist
        Q.remove(u)

        neighbors = (
            (r, c)
            for i, r in enumerate(range(u[0]-1, u[0]+2))
            for j, c in enumerate(range(u[1]-1, u[1]+2))
            if (i + j) % 2 == 1
            if r in range(rows)
            if c in range(cols)
        )

        for v in neighbors:
            v_r, v_c = v
            alt = dist[u] + risk_map[v_r][v_c]

            if alt < dist[v]:
                dist[v] = alt
                heuristic[v] = alt + cost(v, goal)
                if v not in Q:
                    Q.add(v)


with open('input/day_15.txt', 'r') as f:
    risk_map = parse_input(f.read())

    rows, cols = len(risk_map), len(risk_map[0])
    dist = a_star(risk_map, manhattan)
    print(dist[(rows-1, cols-1)])

    full_risk_map = expand_map(risk_map)
    rows, cols = len(full_risk_map), len(full_risk_map[0])
    full_dist = a_star(full_risk_map, manhattan)
    print(full_dist[(rows-1, cols-1)])
