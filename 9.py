with open('input/9.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))


def calc_already_touched(length):
    knots = length * [Pos(0, 0)]
    already_touched = set(knots)

    for line in lines:
        d, step = line.split(' ')
        for i in range(int(step)):
            knots[0] += dirs[d]
            follow(knots, 1)
            already_touched.add(knots[len(knots) - 1])

    return len(already_touched)


def follow(knots, tail_index):
    if tail_index < len(knots):
        x, y = knots[tail_index - 1].x - knots[tail_index].x, knots[tail_index - 1].y - knots[tail_index].y
        if (x * x + y * y) ** 0.5 > 1.5:
            knots[tail_index] += Pos(x / max((int(abs(x) > 1) + 1), 1), y / max((int(abs(y) > 1) + 1), 1))
        follow(knots, tail_index + 1)


dirs = {'R': Pos(1, 0), 'L': Pos(-1, 0), 'U': Pos(0, 1), 'D': Pos(0, -1)}

print(calc_already_touched(2))
print(calc_already_touched(10))
