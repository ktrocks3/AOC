import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

flags = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        if not char.isnumeric() and char != '.':
            flags[i][j] = True

old_flags = [f.copy() for f in flags]
while True:
    for i, line in enumerate(lines):
        for j, char in enumerate(line.strip()):
            nearby_i = [i - 1, i, i + 1]
            nearby_j = [j - 1, j, j + 1]
            nearby_i = [x for x in nearby_i if x >= 0 and x < len(lines)]
            nearby_j = [x for x in nearby_j if x >= 0 and x < len(lines[0])]
            for i2 in nearby_i:
                for j2 in nearby_j:
                    if i2 == i and j2 == j:
                        continue
                    if flags[i2][j2] and char.isnumeric():
                        flags[i][j] = True
    if flags == old_flags:
        break
    old_flags = [f.copy() for f in flags]
result = ""
for i, flag in enumerate(flags):
    for j, f in enumerate(flag):
        if f:
            result += lines[i][j]
        else:
            result += ' '
print(sum([int(x) for x in re.findall(r'\d+', result)]))
