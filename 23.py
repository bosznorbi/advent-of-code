with open('input/23.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

directions = ['N', 'S', 'W', 'E']
move = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
check = {'N': [(-1, 0), (-1, -1), (-1, 1)], 'S': [(1, 0), (1, -1), (1, 1)],
         'W': [(-1, -1), (0, -1), (1, -1)], 'E': [(-1, 1), (0, 1), (1, 1)]}
around = set(sum(check.values(), []))


def is_someone_there(pos, where):
    for i, j in where:
        if (pos[0] + i, pos[1] + j) in elves:
            return True
    return False


def propose_direction(pos):
    for dir in directions:
        if not is_someone_there(pos, check[dir]):
            return move[dir]
    return None


def count_empty_field():
    min_row, min_col = min(elves, key=lambda e: e[0])[0], min(elves, key=lambda e: e[1])[1]
    max_row, max_col = max(elves, key=lambda e: e[0])[0], max(elves, key=lambda e: e[1])[1]
    return (((max_row + 1) - min_row) * ((max_col + 1) - min_col)) - len(elves)


elves = set()
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '#':
            elves.add((row, col))

round_counter = 0
still_going = True
while still_going:
    round_counter += 1
    still_going = False
    proposals = {}
    proposal_count = {}
    for elf in elves:
        if is_someone_there(elf, around):
            proposal = propose_direction(elf)
            if proposal is not None:
                new_place = (elf[0] + proposal[0], elf[1] + proposal[1])
                proposals[elf] = new_place
                proposal_count.setdefault(new_place, 0)
                proposal_count[new_place] = proposal_count[new_place] + 1
    for elf in proposals:
        if proposal_count[proposals[elf]] == 1:
            still_going = True
            elves.remove(elf)
            elves.add(proposals[elf])
    directions.append(directions.pop(0))

    if round_counter == 10:
        print(count_empty_field())

print(round_counter)
