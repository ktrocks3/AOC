from collections import defaultdict

with open('example.txt', 'r') as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))


def get_loc(seed, sections):
    last = seed
    for i, section in enumerate(sections):
        for j, row in enumerate(section):
            if row[1] <= last <= row[1] + row[2]:
                dif = row[0] - row[1]
                last = last + dif
                break
    return last


sections = [[]]
maps = defaultdict(lambda: defaultdict(int))
for line in lines:
    if line == '':
        sections.append([])
    else:
        sections[-1].append(line)
sections[0] = sections[0][0].split(' ')[1:]
seeds = sections.pop(0)
for i, section in enumerate(sections):
    section.pop(0)
    sections[i] = [[int(y) for y in x.split(' ')] for x in section]

locations = []
for s in seeds:
    locations.append(get_loc(int(s), sections))
print(min(locations))
