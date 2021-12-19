# https://adventofcode.com/2021/day/17

def get_target(text):
    text = text.strip().replace('target area: ', '')
    (x_range, y_range) = text.split(', ')
    (x1, x2) = (int(x) for x in x_range.replace('x=', '').split('..'))
    (y1, y2) = (int(y) for y in y_range.replace('y=', '').split('..'))

    return ((x1, x2), (y1, y2))


def iter_trajectory(v):
    loc = (0, 0)
    while True:
        yield loc

        loc = tuple(sum(x) for x in zip(loc, v))
        vx, vy = v
        if vx:
            vx = vx - 1 if (0 < vx) else vx + 1
        v = (vx, vy - 1)


def get_trajectory(target, v):
    ((xt1, xt2), (yt1, yt2)) = target
    trajectory_history = []
    trajectory = iter_trajectory(v)
    hit = False

    while True:
        (xc, yc) = next(trajectory)
        trajectory_history.append((xc, yc))

        if xc in range(xt1, xt2 + 1) and yc in range(yt1, yt2 + 1):
            hit = True
        elif xt2 < xc or yc < yt1:
            break

    return trajectory_history, hit


def get_possible_v(target):
    ((xt1, xt2), (yt1, yt2)) = target

    vx_list = []
    for vx in range(xt2 + 1):
        step = 0
        next_loc = 0
        while True:
            if vx * (vx + 1) // 2 < xt1:
                break
            next_loc += vx-step
            if next_loc in range(xt1, xt2+1):
                vx_list.append(vx)
                break
            elif xt2 < next_loc:
                break
            step += 1

    vy_list = []
    for vy in range(-yt1 + 1):
        step = 0
        next_loc = 0
        while True:
            next_loc -= vy + step + 1
            if next_loc in range(yt1, yt2+1):
                vy_list.append(vy)
                vy_list.append(-vy - 1)
                break
            if next_loc < yt1:
                break
            step += 1

    return (vx_list, vy_list)


def get_highest_v(target):
    vx_list, vy_list = get_possible_v(target)
    v_highest = (min(vx_list), max(vy_list))
    trajectory_highest, _ = get_trajectory(target, v_highest)
    return max(x[1] for x in trajectory_highest)


def get_good_v(target):
    (vx_list, vy_list) = get_possible_v(target)
    good_v = []

    for vx in vx_list:
        for vy in vy_list:
            _, hit = get_trajectory(target, (vx, vy))
            if hit:
                good_v.append((vx, vy))

    return good_v


if __name__ == '__main__':
    with open('input/day_17.txt', 'r') as f:
        target = get_target(f.read())

        print(get_highest_v(target))
        print(len(get_good_v(target)))
