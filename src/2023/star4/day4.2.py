import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

result = defaultdict(int)
copies = defaultdict(int)
numwins = len(lines[0].split(':')[1].split('|')[0].strip().split(' ')) + 1
for line in lines:
    res = re.findall(r'\d+', line)
    card_num = int(res[0])
    copies[card_num] += 1
    winning = res[1:numwins]
    rest = res[numwins:]
    win = len([r for r in rest if r in winning])
    for i in range(card_num+1, card_num + win+1):
        copies[i] += copies[card_num]

print(sum(copies.values()))