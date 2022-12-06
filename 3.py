with open('input/3.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

priorities = {k: ord(k) - ord('a') + 1 for k in 'abcdefghijklmnopqrstuvwxyz'} \
             | {k: ord(k) - ord('A') + 27 for k in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}


def duplicate_priority_sum():
    return sum(map(lambda x: priorities[get_duplicate_item(x)], lines.copy()))


def get_duplicate_item(rucksack):
    return min(set(rucksack[:len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2:]))


def badge_priority_sum():
    counter = 0
    rucksacks = lines.copy()
    while rucksacks:
        counter += priorities[find_badge_in_group(rucksacks[:3])]
        rucksacks = rucksacks[3:]
    return counter


def find_badge_in_group(group):
    return min(set(group[0]) & set(group[1]) & set(group[2]))


print(duplicate_priority_sum())
print(badge_priority_sum())
