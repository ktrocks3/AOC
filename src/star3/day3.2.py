import re

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

flags = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '*':
            flags[i][j] = True
old_flags = [f.copy() for f in flags]
while True:
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
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

total = 0
for i, flag in enumerate(flags):
    for j, f in enumerate(flag):
        nums = []
        if lines[i][j] == '*':
            nearby_i = [i - 1, i, i + 1]
            nearby_j = [j - 1, j, j + 1]
            nearby_i = [x for x in nearby_i if x >= 0 and x < len(lines)]
            nearby_j = [x for x in nearby_j if x >= 0 and x < len(lines[0])]
            same_number = False
            for i2 in nearby_i:
                for j2 in nearby_j:
                    if flags[i2][j2] and lines[i2][j2].isnumeric():
                        if same_number:
                            continue
                        num = lines[i2][j2]
                        inner_j = j2 - 1
                        while inner_j >= 0 and flags[i2][inner_j] and lines[i2][inner_j].isnumeric():
                            num = lines[i2][inner_j] + num
                            inner_j -= 1
                            if inner_j < 0:
                                break
                        inner_j = j2 + 1
                        while inner_j < len(lines[0]) and flags[i2][inner_j] and lines[i2][inner_j].isnumeric():
                            num = num + lines[i2][inner_j]
                            inner_j += 1
                            if inner_j >= len(lines[0]):
                                break
                        num = num.replace('*', '')
                        if num == '':
                            continue
                        nums.append(int(num))
                        same_number = True
                    else:
                        same_number = False
                same_number = False
        if len(nums) == 2:
            print(nums[0], nums[1])
            total += nums[0] * nums[1]

print(total)
