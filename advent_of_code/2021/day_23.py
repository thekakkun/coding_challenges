# https://adventofcode.com/2021/day/23

import copy
import re


class Room:
    def __init__(self, designation, occupants, size=None) -> None:
        if size is None:
            self.size = 2
        self.designation = designation
        self.occupants = occupants

    def __repr__(self) -> str:
        return f'{self.occupants}'

    def get_occupant(self):
        return self.occupants[0] if self.occupants else False

    def is_valid_origin(self):
        if not self.occupants:
            return False
        elif not [o for o in self.occupants if o != self.designation]:
            return False
        else:
            return True

    def leave(self):
        assert self.is_valid_origin()

        moves = self.size + 1 - len(self.occupants)
        amp = self.occupants.pop(0)

        return (amp, moves)

    def is_valid_dest(self, pod):
        if self.designation != pod:
            return False
        elif self.is_valid_origin():
            return False
        elif len(self.occupants) == self.size:
            return False
        else:
            return True

    def enter(self, pod):
        assert self.is_valid_dest(pod)

        moves = self.size + 1 - len(self.occupants)
        self.occupants.insert(0, pod)

        return moves


class Hall:
    def __init__(self, occupant=None) -> None:
        if occupant is None:
            self.occupant = []
        else:
            self.occupant = [occupant]

    def __repr__(self) -> str:
        return f'{self.occupant}'

    def get_occupant(self):
        return self.occupant[0] if self.occupant else False

    def is_valid_origin(self):
        if self.occupant:
            return True
        else:
            return False

    def leave(self):
        assert self.is_valid_origin()
        return (self.occupant.pop(0), 0)

    def is_valid_dest(self, pod=None):
        if self.occupant:
            return False
        else:
            return True

    def enter(self, pod):
        # assert self.is_valid_dest()

        self.occupant.insert(0, pod)
        return 0


class Burrow:
    def __init__(self, text, designations=None, energy=None) -> None:
        if designations is None:
            self.designations = {2: 'A', 4: 'B', 6: 'C', 8: 'D'}
        if energy is None:
            self.energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

        (_, hallway, *rooms, _) = text.strip().splitlines()
        self.length = hallway.count('.')
        self.state = [Hall() for _ in range(self.length)]
        rooms = zip(*[re.findall(r'\w', row) for row in rooms])
        for room, designation in self.designations.items():
            self.state[room] = Room(designation, list(next(rooms)))

        self.energy_used = 0

    def valid_moves(self):
        moves = []
        for src, loc in enumerate(self.state):
            if loc.is_valid_origin():
                dests = self.valid_dests(src)
                if dests:
                    moves.extend((src, dest) for dest in dests)
                else:
                    continue

        return moves

    def valid_dests(self, src):
        if isinstance(self.state[src], Room):
            dests = []
            for i in [src-1, src+1]:
                if self.is_reachable(src, i):
                    dests.append(i)
            return dests

        elif isinstance(self.state[src], Hall):
            pod = self.state[src].get_occupant()
            correct_room = next(
                k for k, v in self.designations.items() if v == pod)
            if (self.state[correct_room].is_valid_dest(pod) and
                    self.is_reachable(src, correct_room)):
                return [correct_room]

    def is_reachable(self, src, dest):
        blocked = self.get_blocked(src, dest)
        freespace = (self.get_freespace(dest, self.length-1)
                     if (src < dest)
                     else self.get_freespace(dest, 0))

        return len(blocked) <= len(freespace)

    def make_move(self, src, dest):
        assert self.is_reachable(src, dest)

        direction = +1 if (src < dest) else -1
        while True:
            blockers = self.get_blocked(src, dest)
            if not blockers:
                break
            self.scooch(blockers[0], direction)

        pod, leave_moves = self.state[src].leave()
        enter_moves = self.state[dest].enter(pod)
        self.energy_used += (leave_moves + abs(src-dest) +
                             enter_moves) * self.energy[pod]

    def get_blocked(self, src, dest):
        direction = +1 if (src < dest) else -1

        return [i for i in range(src + direction, dest + direction, direction)
                if isinstance(self.state[i], Hall)
                if not self.state[i].is_valid_dest()]

    def get_freespace(self, src, dest):
        direction = +1 if (src < dest) else -1

        return [i for i in range(src + direction, dest + direction, direction)
                if isinstance(self.state[i], Hall)
                if self.state[i].is_valid_dest()]

    def scooch(self, i, direction):
        pod = self.state[i].get_occupant()
        dest = i + direction
        while True:
            if self.state[dest].is_valid_dest(pod):
                self.make_move(i, dest)
                break
            elif isinstance(self.state[dest], Room):
                dest += direction
            elif isinstance(self.state[dest], Hall):
                self.scooch(dest, direction)

        return dest

    def hallway_occupants(self):
        return sum(1 for loc in self.state
                   if isinstance(loc, Hall)
                   if loc.get_occupant())

    def organized(self):
        for loc in self.state:
            if isinstance(loc, Hall):
                if loc.occupant:
                    return False
            elif isinstance(loc, Room):
                if loc.occupants.count(loc.designation) != loc.size:
                    return False
        else:
            return True


def get_successors(burrow):
    successors = []
    moves = burrow.valid_moves()
    for move in moves:
        result = copy.deepcopy(burrow)
        result.make_move(*move)
        successors.append(result)

    return sorted(successors,
                  key=lambda x: (x.energy_used))


def organize(burrow):
    paths = set()
    frontier = [burrow]
    while frontier:
        frontier.sort(key=lambda x: (x.energy_used))
        b_state = frontier.pop(0)
        paths.add(b_state)
        successors = get_successors(b_state)

        for s in successors:
            if s in paths:
                continue
            elif s.organized():
                return s.energy_used
            else:
                print(s.state, s.energy_used)
                frontier.append(s)


def main():
    with open('input/day_23.txt', 'r') as f:
        burrow = Burrow(f.read())
        print(organize(burrow))


if __name__ == '__main__':
    main()
