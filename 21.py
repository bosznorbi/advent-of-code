from sympy import symbols, solve

with open('input/21.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()


def get_value(key):
    value = storage[key]
    if value.isnumeric():
        return int(value)
    else:
        first, operator, second = value.split(' ')
        return int(eval(str(get_value(first)) + operator + str(get_value(second))))


def fix_values(key):
    value = storage[key]
    if value.isnumeric():
        return int(value)
    else:
        first, operator, second = value.split(' ')
        value = int(eval(str(fix_values(first)) + operator + str(fix_values(second))))
        if first in variables:
            variables.add(key)
            storage[key] = first + ' ' + operator + ' ' + str(fix_values(second))
        elif second in variables:
            variables.add(key)
            storage[key] = str(fix_values(first)) + ' ' + operator + ' ' + second
        else:
            storage[key] = str(value)
        return value


def get_expression(key):
    value = storage[key]
    if value == 'x':
        return 'x'
    if value.isnumeric():
        return int(value)
    else:
        first, operator, second = value.split(' ')
        if first in variables:
            return '(' + str(get_expression(first)) + ') ' + operator + ' ' + second
        if second in variables:
            return first + ' ' + operator + ' (' + str(get_expression(second)) + ')'


storage = {}
variables = {'humn'}

for line in lines:
    name, eq = line.split(': ')
    storage[name] = eq

print(get_value('root'))

fix_values('root')
storage['humn'] = 'x'
storage['root'] = '32853424641061 - pnhm'
x = symbols('x')
print(solve(get_expression('root'))[0])
