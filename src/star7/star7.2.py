from functools import cmp_to_key

with open('input.txt', 'r') as f:
    lines = list(map(lambda x: x.strip().split(' '), f.readlines()))

ORDER = "AKQT98765432J"


def generate_permutations(card, cards="AKQT98765432"):
    if 'J' not in card:
        return [card]
    else:
        permutations = []
        j_index = card.index('J')
        for c in cards:
            # Replace the first occurrence of 'J' with each card
            replaced = card[:j_index] + c + card[j_index + 1:]
            # Recursively generate permutations for the new string
            permutations.extend(generate_permutations(replaced, cards))
        return permutations


def card_type(card):
    high = 'a'
    for c in generate_permutations(card):
        unique = list(set(c))
        if len(unique) == 1:
            return 'z'
        elif len(unique) == 2:
            if c.count(unique[0]) == 4 or c.count(unique[0]) == 1:
                high = max(high, 'y')
            else:
                high = max(high, 'x')
        elif len(unique) == 3:
            if c.count(unique[0]) == 3 or c.count(unique[1]) == 3 or c.count(unique[2]) == 3:
                high = max(high, 'w')
            else:
                high = max(high, 'v')
        elif len(set(c)) == 4:
            high = max(high, 'u')
        else:
            high = max(high, 't')
    return high


def compare(card1, card2):
    if card1 == card2:
        return 0
    if card_type(card1) > card_type(card2):
        return 1
    elif card_type(card1) < card_type(card2):
        return -1
    else:
        for i in range(len(card1)):
            if ORDER.index(card1[i]) < ORDER.index(card2[i]):
                return 1
            elif ORDER.index(card1[i]) > ORDER.index(card2[i]):
                return -1


sorted_lines = sorted(lines, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
total = 0

for i, (card, bet) in enumerate(sorted_lines):
    total += (i + 1) * int(bet)
print(total)

print(card_type('32T3K'))
print(card_type('KK677'))
print(card_type('T55J5'))
print(card_type('KTJJT'))
print(card_type('QQQJA'))
