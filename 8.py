with open('input/8.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


class Tree:
    def __init__(self, size, x, y):
        self.size = size
        self.visible = False
        self.scenic = 0
        self.x = x
        self.y = y

    def __repr__(self):
        if self.visible:
            return str(self.size)
        else:
            return '.'


def evaluate():
    evaluate_from_corner()
    reverse()
    evaluate_from_corner()
    reverse()


def evaluate_from_corner():
    col_max = []
    row_max = []
    for row in range(height):
        for col in range(width):
            tree = trees[row][col]
            if col == 0:
                row_max.append(tree.size)
                tree.visible = True
            if row == 0:
                col_max.append(tree.size)
                tree.visible = True
            else:
                if tree.size > col_max[col]:
                    tree.visible = True
                    col_max[col] = tree.size
                if tree.size > row_max[row]:
                    tree.visible = True
                    row_max[row] = tree.size


def reverse():
    trees.reverse()
    for r in trees:
        r.reverse()


trees = []

for i, line in enumerate(lines):
    trees.append([])
    j = 0
    for char in line.strip():
        j += 1
        trees[i].append(Tree(int(char), i, j))

height = len(trees)
width = len(trees[0])


def scenic():
    for row in range(height):
        for col in range(width):
            left = right = up = down = 1

            while 0 < col - left and trees[row][col - left].size < trees[row][col].size:
                left += 1
            while col + right < width - 1 and trees[row][col + right].size < trees[row][col].size:
                right += 1
            while 0 < row - down and trees[row - down][col].size < trees[row][col].size:
                down += 1
            while row + up < height - 1 and trees[row + up][col].size < trees[row][col].size:
                up += 1

            if row == 0:
                left = 0
            if col == 0:
                up = 0
            if row == width - 1:
                right = 0
            if col == height - 1:
                down = 0

            trees[row][col].scenic = left * right * up * down


evaluate()
print(sum(1 for x in sum(trees.copy(), []) if x.visible))

scenic()
max_scenic = max(sum(trees.copy(), []), key=lambda x: x.scenic)
print(max_scenic.scenic)
