class UniqueInteger:
    def __init__(self, value):
        self.value = value


with open('input/20.txt') as f:
    lines = [int(s.strip()) for s in f.readlines()]
f.close()


def calc_grove(times=1, decr_number=1):
    lines_copy = [UniqueInteger(x * decr_number) for x in lines]
    lines_original = lines_copy.copy()
    for i in range(times):
        for line in lines_original:
            i = lines_copy.index(line)
            lines_copy.remove(line)
            lines_copy.insert((i + line.value) % (len(lines_copy)), line)

    index_of_0 = get_index_of_0(lines_copy)
    return (lines_copy[(index_of_0 + 1000) % len(lines_copy)].value
            + lines_copy[(index_of_0 + 2000) % len(lines_copy)].value
            + lines_copy[(index_of_0 + 3000) % len(lines_copy)].value)


def get_index_of_0(array):
    for i, element in enumerate(array):
        if element.value == 0:
            return i


print(calc_grove())
print(calc_grove(10, 811589153))
