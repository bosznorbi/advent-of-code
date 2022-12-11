with open('input/10.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def strength(c):
    return c * values[c - 1]


def get_lamp_char(c):
    return '#' if values[c - 1] <= c % 40 <= values[c - 1] + 2 else '.'


values = [1]
cycle = 0
for line in lines:
    values.append(values[cycle])
    cycle += 1
    cmd = line[4:].strip()
    if len(cmd) > 0:
        values.append(values[cycle] + int(cmd))
        cycle += 1

print(sum([strength(i * 40 + 20) for i in range(6)]))
for i in range(6):
    print(''.join([get_lamp_char(i * 40 + j + 1) for j in range(39)]))
