with open('input/8.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


class Tree:
    def __init__(self, size):
        self.size = size
        self.see = False

    def __gt__(self, other):
        return self.size > other.size


def calc_see_from_top_left(array):
    for row in array:
        for i in range(len(row)):
            row[i].see = row[i].see or min(max(row[:i], default=Tree(-1)), max(row[i + 1:], default=Tree(-1))) < row[i]


def get_highest_scenic():
    max_scenic = 0
    for row in range(len(trees)):
        for col in range(len(trees[0])):
            if not (row == 0 or col == 0 or row == (len(trees[0]) - 1) or col == (len(trees) - 1)):
                scenic = 1
                for d1, d2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    value = 1
                    while (0 < col + (d1 * value) < len(trees[0]) - 1) and (0 < row + (d2 * value) < len(trees) - 1) \
                            and trees[row + (d2 * value)][col + (d1 * value)].size < trees[row][col].size:
                        value += 1
                    scenic *= value
                max_scenic = max(max_scenic, scenic)
    return max_scenic


trees = [list(map(lambda ch: Tree(int(ch)), line)) for line in lines]
calc_see_from_top_left(trees)
calc_see_from_top_left([*zip(*trees)])

print(sum(1 for x in sum(trees, []) if x.see))
print(get_highest_scenic())
