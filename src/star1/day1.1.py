with open('input.txt', 'r') as f:
    lines = f.readlines()

res = []
for line in lines:
    a = [x for x in line if x.isdigit()]
    res.append(a[0] + a[-1])

print(sum([int(x) for x in res]))