import re

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

time = int(''.join(re.findall(r'\d+', lines[0])))
distances = int(''.join(re.findall(r'\d+', lines[1])))

window_size = time // 100
nwins = 0
last = ''
vals = []
for i in range(0, time, window_size):
    if last != ('yes' if (time - i) * i > distances else 'no'):
        vals.append(i)
        last = 'yes' if (time - i) * i > distances else 'no'
vals.pop(0)
last = ''
nvals = []
for v in vals:
    for i in range(v-window_size, v+window_size):
        if last != ('yes' if (time - i) * i > distances else 'no'):
            nvals.append(i)
            last = 'yes' if (time - i) * i > distances else 'no'
print(nvals[-1] - nvals[-2])
