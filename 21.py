with open('input/21.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def get_value(key):
    value = storage[key]
    if value.isnumeric():
        return int(value)
    else:
        first, operator, second = value.split(' ')
        return eval(str(get_value(first)) + operator + str(get_value(second)))


storage = {}

for line in lines:
    name, eq = line.split(': ')
    storage[name] = eq

print(int(get_value('root')))
