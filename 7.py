with open('input/7.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


class Dir:
    def __init__(self, parent):
        self.content = {}
        self.parent = parent
        self.size = 0
        dirs.add(self)

    def add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)


dirs = set()
root = Dir(None)
pointer = None

for line in lines:
    line = line.replace('$ ', '').split(' ')
    if line[0] == 'ls':
        continue
    cmd, name = line
    if cmd == 'cd':
        if name == '/':
            pointer = root
        elif name == '..':
            pointer = pointer.parent
        elif name.isalpha():
            pointer = pointer.content[name]
    elif cmd == 'dir':
        pointer.content[name] = Dir(pointer)
    elif cmd.isnumeric():
        pointer.content[name] = cmd
        pointer.add_size(int(cmd))


def count_small_dir_sizes(limit):
    return sum(d.size for d in filter(lambda d: d.size <= limit, dirs))


def find_smallest_deletable(clear_needed):
    return next(size for size in sorted(map(lambda x: x.size, dirs)) if size >= clear_needed)


print(count_small_dir_sizes(100000))
print(find_smallest_deletable(root.size - 40000000))
