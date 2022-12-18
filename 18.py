import numpy as np
import scipy.ndimage as ndi

with open('input/18.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def count_surface(cube_list):
    surface = 0
    counted_cubes = []
    for a, b, c in cube_list:
        counted_cubes.append((a, b, c))
        surface += 6
        for x, y, z in [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            if (a + x, b + y, c + z) in counted_cubes:
                surface -= 2
    return surface


def get_filled_cubes(cube_list):
    binary_cube_map = []
    for i in range(20):
        binary_cube_map.append([])
        for j in range(20):
            binary_cube_map[i].append([])
            for k in range(20):
                binary_cube_map[i][j].append(True if (i, j, k) in cube_list else False)

    filled_binary_cube_map = ndi.binary_fill_holes(np.array(binary_cube_map))
    filled_cubes = []
    for i in range(20):
        for j in range(20):
            for k in range(20):
                if filled_binary_cube_map[i][j][k]:
                    filled_cubes.append((i, j, k))
    return filled_cubes


cubes = [tuple(map(int, line.split(','))) for line in lines]

print(count_surface(cubes))
print(count_surface(get_filled_cubes(cubes)))
