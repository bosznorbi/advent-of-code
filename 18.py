with open('input/18.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

cubes = []
surface = 0
neighbor_dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
for line in lines:
    a, b, c = map(int, line.split(','))
    cubes.append((a, b, c))
    surface += 6
    for x, y, z in neighbor_dirs:
        if (a + x, b + y, c + z) in cubes:
            surface -= 2

print(surface)
