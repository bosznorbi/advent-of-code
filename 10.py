with open('input/10.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

values = [0, 1]
cycle = 1
for line in lines:
    values.append(values[cycle])
    line = line.split(' ')
    if line[0] == 'addx':
        cycle += 1
        values.append(values[cycle] + int(line[1]))
    cycle += 1


def strength(i):
    return i * values[i]


print(strength(20) + strength(60) + strength(100) + strength(140) + strength(180) + strength(220))


def get_lamp_char(cycle):
    if values[cycle] <= cycle % 40 <= values[cycle] + 2:
        return '#'
    return '.'


for i in range(6):
    s = ''
    for j in range(40):
        s += get_lamp_char(i * 40 + j + 1)
    print(s)
