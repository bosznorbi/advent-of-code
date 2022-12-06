def find_start(count, s):
    for i in range(len(s)):
        if len(s[:count]) == len(set(s[:count])):
            return i + count
        s = s[1:]


signal = open('input/6.txt').read().strip()
print(find_start(4, signal))
print(find_start(14, signal))
