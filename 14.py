import numpy as np

with open('input/14.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def build_rocks():
    rocks = {}
    for line in lines:
        corners = line.split(' -> ')
        for i in range(1, len(corners)):
            col, row = map(int, corners[i].split(','))
            prev_col, prev_row = map(int, corners[i - 1].split(','))
            for x in get_inclusive_range(col, prev_col):
                for y in get_inclusive_range(row, prev_row):
                    rocks.setdefault(x, set()).add(y)
    return rocks


def build_rocks_with_floor():
    rocks = build_rocks()
    floor = get_floor(rocks)
    for col in get_inclusive_range(SAND_COL - floor, SAND_COL + floor):
        rocks.setdefault(col, set()).add(floor)
    return rocks


def build_sands(rocks):
    floor = get_floor(rocks)
    sands = {}
    overflow = False
    while not overflow and not (SAND_COL in sands and SAND_ROW in sands[SAND_COL]):
        rested = False
        col, row = SAND_COL, SAND_ROW
        while not rested and not overflow:
            if row > floor:
                overflow = True
            else:
                moved = False
                for i in [0, -1, 1]:
                    if not moved:
                        if not (col + i in rocks and row + 1 in rocks[col + i]):
                            if not (col + i in sands and row + 1 in sands[col + i]):
                                col += i
                                row += 1
                                moved = True
                if not moved:
                    sands.setdefault(col, set()).add(row)
                    rested = True
    return sands


def get_floor(rocks):
    return max({x for v in rocks.values() for x in v}) + 2


def get_sand_count(sands):
    return len([x for v in sands.values() for x in v])


def get_inclusive_range(start, end):
    return range(start, end + (np.sign(end - start) or 1), np.sign(end - start) or 1)


def draw(rocks, sands):
    for row in get_inclusive_range(SAND_ROW, get_floor(rocks)):
        s = ''
        for col in get_inclusive_range(min(rocks), max(rocks)):
            s += '#' if (col in rocks and row in rocks[col]) else ('o' if (col in sands and row in sands[col]) else '.')
        print(s)


SAND_COL, SAND_ROW = 500, 0

rocks_no_floor = build_rocks()
sands_no_floor = build_sands(rocks_no_floor)
print(get_sand_count(sands_no_floor))

rocks_with_floor = build_rocks_with_floor()
sands_with_floor = build_sands(rocks_with_floor)
print(get_sand_count(sands_with_floor))

# draw(rocks_no_floor, sands_no_floor)
# draw(rocks_with_floor, sands_with_floor)
