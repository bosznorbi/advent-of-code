shifts = open('input/17.txt').read().strip()


class Rock:
    def __init__(self, row, shape):
        self.rested = False
        if shape == 0:  # -
            self.bits = [(0, 0), (0, 1), (0, 2), (0, 3)]
            self.place = (row + 1, 2)
        elif shape == 1:  # L
            self.bits = [(-2, 1), (-1, 0), (-1, 1), (-1, 2), (0, 1)]
            self.place = (row + 3, 2)
        elif shape == 2:  # +
            self.bits = [(-2, 0), (-2, 1), (-2, 2), (-1, 2), (0, 2)]
            self.place = (row + 3, 2)
        elif shape == 3:  # I
            self.bits = [(-3, 0), (-2, 0), (-1, 0), (0, 0)]
            self.place = (row + 4, 2)
        elif shape == 4:  # O
            self.bits = [(-1, 0), (-1, 1), (0, 0), (0, 1)]
            self.place = (row + 2, 2)

    def move(self, dir):
        for i, j in self.bits:
            x, y = self.place[0] + i + dir[0], self.place[1] + j + dir[1]
            if x < 0 or y < 0 or y > 6 or (x, y) in rocks:
                return False
        self.place = (self.place[0] + dir[0], self.place[1] + dir[1])
        return True

    def fall(self):
        if not self.move((-1, 0)):
            self.rested = True
            for i, j in self.bits:
                rocks.add((self.place[0] + i, self.place[1] + j))


def count_rows(turns):
    top_row = -1
    shift_counter = 0
    for turn in range(turns):
        rock = Rock(top_row + 3, turn % 5)
        while not rock.rested:
            rock.move((0, 1) if shifts[shift_counter % len(shifts)] == '>' else (0, -1))
            shift_counter += 1
            rock.fall()
        top_row = max(top_row, rock.place[0])
    return top_row + 1


rocks = set()
print(count_rows(2022))
