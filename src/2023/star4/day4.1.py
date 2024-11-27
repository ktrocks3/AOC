import re
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

result = defaultdict(int)
numwins = len(lines[0].split(':')[1].split('|')[0].strip().split(' ')) + 1
for line in lines:
    res = re.findall(r'\d+', line)
    card_num = res[0]
    winning = res[1:numwins]
    rest = res[numwins:]
    for r in rest:
        if r in winning:
            if result[card_num] == 0:
                result[card_num] = 1
            else:
                result[card_num] *= 2
print(sum(result.values()))