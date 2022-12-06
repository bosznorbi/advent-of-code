with open('input/4.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

fully_overlap = 0
overlap = 0
for line in lines:
    a1, a2, b1, b2 = list(map(int, line.replace(',', '-').split('-')))
    if max(a1, b1) <= min(a2, b2):
        overlap += 1
        if (a1 <= b1 and b2 <= a2) or (b1 <= a1 and a2 <= b2):
            fully_overlap += 1

print(fully_overlap)
print(overlap)
