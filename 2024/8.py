from collections import defaultdict
from itertools import permutations

data = defaultdict(list)
input = [l.strip() for l in open('data/8.in')]
max_r, max_c = len(input), len(input[0])
antinodes = set()

for r, l in enumerate(input):
    for c, s in enumerate(l):
        if s != '.':
            data[s].append((r,c))

for v in data.values():
    for (x1, y1), (x2, y2) in permutations(v, 2):
        dx, dy = x2 - x1, y2 - y1
        antinodes.add((x1-dx, y1-dy))
        antinodes.add((x2+dx, y2+dy))

print(len({(x,y) for (x,y) in antinodes if 0 <= x < max_r and 0 <= y < max_c}))

antinodes = set()
for v in data.values():
    for (x1, y1), (x2, y2) in permutations(v, 2):
        antinodes.add((x1, y1))
        antinodes.add((x2, y2))
        dx, dy = x2 - x1, y2 - y1
        while 0 <= x1 - dx < max_r and 0 <= y1-dy < max_c:
            x1 -= dx
            y1 -= dy
            antinodes.add((x1, y1))
        while 0 <= x2 + dx < max_r and 0 <= y2 + dy < max_c:
            x2 += dx
            y2 += dy
            antinodes.add((x2, y2))
print(len({(x,y) for (x,y) in antinodes if 0 <= x < max_r and 0 <= y < max_c}))
