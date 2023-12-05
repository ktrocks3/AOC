import re

with open('input.txt', 'r') as f:
    lines = f.readlines()


amounts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total = []
for line in lines:
    game_id_match = re.search(r'Game (\d+)', line)
    if game_id_match:
        game_id = game_id_match.group(1)
    else:
        continue  # Skip to the next iteration if the game ID is not found
    green = max([int(x.split(' ')[0]) for x in re.findall(r'\d+ green', line)])
    if green > amounts['green']:
        continue
    red = max([int(x.split(' ')[0]) for x in re.findall(r'\d+ red', line)])
    if red > amounts['red']:
        continue
    blue = max([int(x.split(' ')[0]) for x in re.findall(r'\d+ blue', line)])
    if blue > amounts['blue']:
        continue
    total.append(int(game_id))
print(total)
print(sum(total))
