from ast import literal_eval

with open('input/13.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def compare(a, b):
    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])
    for x, y in zip(a, b):
        if isinstance(x, int) and isinstance(y, int):
            result = x - y
        else:
            result = compare(x, y)
        if result != 0:
            return result
    return len(a) - len(b)


groups = [[]]
for line in lines:
    if line:
        groups[len(groups) - 1].append(literal_eval(line))
    else:
        groups.append([])

index_sum = 0
for i, (left, right) in enumerate(groups):
    if compare(left, right) < 0:
        index_sum += (i + 1)
print(index_sum)
