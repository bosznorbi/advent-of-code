with open('input/1.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

elf_index = 0
calories = [0]
for line in lines:
    if line:
        calories[elf_index] = int(calories[elf_index]) + int(line)
    else:
        elf_index += 1
        calories.append(0)

print(max(calories))
print(sum(sorted(calories, reverse=True)[:3]))
