with open('input/5.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def dumb_crane(stacks):
    for line in lines:
        move, fr, to = get_values(line)
        for i in range(move):
            stacks[to] += stacks[fr][-1:]
            stacks[fr] = stacks[fr][:-1]
    return on_the_top(stacks)


def smart_crane(stacks):
    for line in lines:
        move, fr, to = get_values(line)
        stacks[to] += stacks[fr][-move:]
        stacks[fr] = stacks[fr][:-move]
    return on_the_top(stacks)


def get_values(line):
    values = line.split(' ')
    move, fr, to = int(values[1]), int(values[3]) - 1, int(values[5]) - 1
    return move, fr, to


def on_the_top(result_stacks):
    s = ''
    for stack in result_stacks:
        s += stack[-1:][0]
    return s


starting_stacks = ['SZPDLBFC', 'NVGPHWB', 'FWBJG', 'GJNFLWCS', 'WJLZPMSH', 'BCWGFS', 'HTPMQBW', 'FSWT', 'NCR']
print(dumb_crane(starting_stacks.copy()))
print(smart_crane(starting_stacks.copy()))
