import copy
import math

with open('input/11.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


class Monkey:
    def __init__(self, _items, _test, _div, _throw_t, _throw_f):
        self.items = _items
        self.test = _test
        self.div = _div
        self.throw_t = _throw_t
        self.throw_f = _throw_f
        self.inspections = 0


def play_keep_away(rounds, relief, monkey_list):
    lcm = math.lcm(*[x.div for x in monkey_list])
    for i in range(rounds):
        for monkey in monkey_list:
            for item in monkey.items:
                worry = (int(eval(str(item) + monkey.test) / relief)) % lcm
                monkey_list[monkey.throw_t if worry % monkey.div == 0 else monkey.throw_f].items.append(worry)
                monkey.inspections += 1
            monkey.items = []
    return math.prod(sorted(list(map(lambda x: x.inspections, monkey_list)))[-2:])


monkeys = []
for line_group in [lines[i * 7:][:7] for i in range(int(len(lines) / 7 + 0.99))]:
    items = [int(x) for x in line_group[1][16:].split(', ')]
    test = line_group[2][20:].replace('* old', '** 2')
    div = int(line_group[3][19:])
    throw_t = int(line_group[4][-1:])
    throw_f = int(line_group[5][-1:])
    monkeys.append(Monkey(items, test, div, throw_t, throw_f))

print(play_keep_away(20, 3, copy.deepcopy(monkeys)))
print(play_keep_away(10000, 1, copy.deepcopy(monkeys)))
