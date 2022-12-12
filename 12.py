with open('input/12.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def swap_char(fr, to):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == fr:
                lines[i] = lines[i].replace(fr, to)
                return i, j


def build_graph():
    g = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            point_to = []
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + a < len(lines) and 0 <= j + b < len(lines[0]):
                    if ord(lines[i][j]) + 1 >= ord(lines[i + a][j + b]):
                        point_to.append(((i + a), (j + b)))
            g[(i, j)] = point_to
    return g


def bfs_min_steps(g, s, e):
    explored = []
    queue = [[s]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            for neighbour in g[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == e:
                    return len(new_path) - 1
            explored.append(node)
    return 9999


def inefficient_bfs_for_all_fields(g, e):
    min_steps = 9999
    for i, j in g:
        if lines[i][j] == 'a':
            min_steps = min(bfs_min_steps(g, (i, j), e), min_steps)
    return min_steps


start, end = swap_char('S', 'a'), swap_char('E', 'z')
graph = build_graph()

print(bfs_min_steps(graph, start, end))
print(inefficient_bfs_for_all_fields(graph, end))
