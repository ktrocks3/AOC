with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip().split(' '), f.readlines()))


def sort_key(card_string):
    return [ORDER.index(card) for card in card_string if card in ORDER]


types = {
    'five': [],
    'four': [],
    'full': [],
    'three': [],
    'two': [],
    'one': [],
    'high': []
}

for card, bet in lines:
    unique = list(set(card))
    if len(unique) == 1:
        types['five'].append((card, bet))
    elif len(unique) == 2:
        if card.count(unique[0]) == 4 or card.count(unique[0]) == 1:
            types['four'].append((card, bet))
        else:
            types['full'].append((card, bet))
    elif len(unique) == 3:
        if card.count(unique[0]) == 3 or card.count(unique[1]) == 3 or card.count(unique[2]) == 3:
            types['three'].append((card, bet))
        else:
            types['two'].append((card, bet))
    elif len(set(card)) == 4:
        types['one'].append((card, bet))
    else:
        types['high'].append((card, bet))
ORDER = "AKQJT98765432"

for type in types:
    types[type].sort(key=lambda x: (sort_key(x[0]), x[1]))

strength = []
for type in types:
    for card, bet in types[type]:
        strength.append(bet)
total = 0
strength.reverse()
for i, bet in enumerate(strength):
    total += (i + 1) * int(bet)
print(total)
