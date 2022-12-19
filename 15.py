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

    def can_reach(self, x, y):
        return self.steps >= abs(self.x - x) + abs(self.y - y)

    def covered(self, row):
        covered = set()
        distance = abs(row - self.y)
        for i in range(-(self.steps - distance), self.steps - distance + 1):
            covered.add(self.x + i)
        return covered


def covered_in_row(checked_row):
    covered = set()
    for sensor in sensors:
        covered.update(sensor.covered(checked_row))
    beacons_in_row = 0
    for beacon in beacons:
        beacons_in_row += 1 if beacon[1] == checked_row else 0
    return len(covered) - beacons_in_row


def find_hidden_beacon():
    for sensor in sorted(sensors, key=lambda s: s.steps):
        edge = sensor.steps + 1
        for i in range(-edge, edge + 1):
            j = edge - abs(i)
            x, y = sensor.x + i, sensor.y + j
            if not can_any_sensors_reach(x, y) and not is_outer(x, y):
                return x, y
            j = -edge + abs(i)
            x, y = sensor.x + i, sensor.y + j
            if not can_any_sensors_reach(x, y) and not is_outer(x, y):
                return x, y


def is_outer(x, y):
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if not can_any_sensors_reach(x + i, y + j):
            return True
    return False


def can_any_sensors_reach(x, y):
    for sensor in sensors:
        if sensor.can_reach(x, y):
            return True
    return False


sensors = []
beacons = set()
for line in lines:
    s, b = line.split(': closest beacon is at x=')
    s_x, s_y = map(int, s.strip('Sensor at x=').split(', y='))
    b_x, b_y = map(int, b.split(', y='))
    sensors.append(Sensor(s_x, s_y, b_x, b_y))
    beacons.add((b_x, b_y))

print(covered_in_row(2000000))

hidden_beacon = find_hidden_beacon()
print(4000000 * hidden_beacon[0] + hidden_beacon[1])
