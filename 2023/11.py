from itertools import combinations
data = [list(l.strip()) for l in open('data/11.in')]

empty_rows = [i for i, l in enumerate(data) if all(s=='.' for s in l)]
empty_cols = [i for i, l in enumerate([all([s[i]=='.' for s in data]) for i in range(len(data[0]))]) if l]

for r in empty_rows[::-1]:
    data.insert(r,['.'] * len(data[0]))

for c in empty_cols[::-1]:
    for d in data:
        d.insert(c+1, '.')

galaxies = []
for r, l in enumerate(data):
    for c, s in enumerate(l):
        if s == "#":
            galaxies.append((r,c))

P1 = 0
for (ax,ay),(bx,by) in combinations(galaxies, 2):
    d = abs(ax-bx) + abs(ay-by)
    P1 += d
print(P1)


