with open('input/7.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

big_dirs = set()
small_dirs = set()

class Dir():
    def __init__(self, parent):
        self.content = {}
        self.parent = parent
        self.size = 0
        small_dirs.add(self)

    def __getitem__(self, item):
        return self.content

    def __str__(self):
        return self.content

    def add_size(self, size):
        self.size += size
        if self.size >= 100000:
            big_dirs.add(self)
            small_dirs.discard(self)
        if self.parent != '':
            self.parent.add_size(size)


pointer = None
tree = {'/': Dir('')}

for line in lines:
    line = line.replace('$ ', '').split(' ')
    if line[0] == 'cd':
        if line[1] == '/':
            pointer = tree.get('/')
        elif line[1] == '..':
            pointer = pointer.parent
        elif line[1].isalpha():
            pointer = pointer.content[line[1]]
    elif line[0] == 'dir':
        pointer.content[line[1]] = Dir(pointer)
    elif line[0].isnumeric():
        pointer.content[line[1]] = line[0]
        pointer.add_size(int(line[0]))

print(sum(int(dir.size) for dir in small_dirs))
clear_needed = tree['/'].size - 70000000 + 30000000
for d in sorted(map(lambda x: x.size, big_dirs)):
    if d > clear_needed:
        print(d)
        break
