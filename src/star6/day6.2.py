import re

with open('example.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

times = int(''.join(re.findall(r'\d+', lines[0])))
distances = int(''.join(re.findall(r'\d+', lines[1])))

nwins = 0
for i in range(times):
    nwins += 1 if (times - i) * i > distances else 0
print(nwins)