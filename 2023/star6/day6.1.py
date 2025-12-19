import re

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

times = list(map(int, re.findall(r'\d+', lines[0])))
distances = list(map(int, re.findall(r'\d+', lines[1])))
total = 1
for i in range(len(distances)):
    nwins = 0
    for j in range(times[i]):
        nwins += 1 if (times[i] - j) * j > distances[i] else 0
    total *= nwins
print(total)
