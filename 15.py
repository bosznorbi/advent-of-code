with open('input/15.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


class Sensor:
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.bx = bx
        self.by = by
        self.steps = abs(x - bx) + abs(y - by)

    def covered(self, row):
        cov = set()
        distance = abs(row - self.y)
        for i in range(-(self.steps - distance), self.steps - distance + 1):
            cov.add(self.x + i)
        return cov

    def __repr__(self):
        return '[' + str(self.x) + ':' + str(self.y) + ', s: ' + str(self.steps) + ']'


sensors = []
beacons = set()
for line in lines:
    s, b = line.split(': closest beacon is at x=')
    s_x, s_y = map(int, s.strip('Sensor at x=').split(', y='))
    b_x, b_y = map(int, b.split(', y='))
    sensors.append(Sensor(s_x, s_y, b_x, b_y))
    beacons.add((b_x, b_y))


def covered_in_row(checked_row):
    covered = set()
    for sensor in sensors:
        covered.update(sensor.covered(checked_row))
    beacons_in_row = 0
    for beacon in beacons:
        beacons_in_row += 1 if beacon[1] == checked_row else 0
    return len(covered) - beacons_in_row


print(covered_in_row(2000000))
