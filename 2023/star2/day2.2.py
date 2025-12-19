import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

amounts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

powers = []
for line in lines:
    green = max([int(x.split(' ')[0]) for x in re.findall(r'\d+ green', line)])
    red = max([int(x.split(' ')[0]) for x in re.findall(r'\d+ red', line)])
    blue = max([int(x.split(' ')[0]) for x in re.findall(r'\d+ blue', line)])
    powers.append(int(green) * int(red) * int(blue))
print(sum(powers))
