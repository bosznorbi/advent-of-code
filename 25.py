with open('input/25.txt') as f:
    lines = [s.strip() for s in f.readlines()]
f.close()

s_to_d = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
d_to_s = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}


def dec_to_snafu(dec):
    snafu = ''
    while dec > 0:
        snafu += d_to_s[dec % 5]
        dec = (2 + dec) // 5
    return snafu[::-1]


sum = 0
for line in lines:
    for i, c in enumerate(reversed(line)):
        sum += ((s_to_d[c]) * (5 ** i))

print(dec_to_snafu(sum))
