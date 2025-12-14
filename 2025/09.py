from itertools import combinations
from collections import deque
from tqdm import tqdm

data = [[int(n) for n in l.strip().split(',')] for l in open('data/9.in')]

def area(a, b):
    return (abs(b[1] - a[1]) + 1) * (abs(b[0] - a[0]) + 1)

P1 = max(area(c1, c2) for c1, c2 in combinations(data, 2))
print(P1)

all_areas = sorted([(area(c1, c2), c1, c2) for c1, c2 in combinations(data, 2)], reverse=True)
data = data + [data[0]]

perimiter = set()
for (r1, c1), (r2, c2) in zip(data, data[1:]):
    for r in range(min(r1, r2), max(r1, r2) + 1):
        for c in range(min(c1, c2), max(c1, c2) + 1):
            perimiter.add((r,c))

_, sr, sc = sorted([(r + c, r, c) for r, c in data])[0]
S = sr - 1, sc - 1

q = deque([S])
outer_perimeter = {S}
visited = {S}
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
extended_dirs = dirs + [(1,1),(1,-1),(-1,1),(-1,-1)]
while q:
    r, c = q.popleft()

    for dr, dc in dirs:
        next_node = nr, nc = r + dr, c + dc

        if next_node in perimiter or next_node in outer_perimeter or next_node in visited:
            continue

        for dr, dc in extended_dirs:
            next_next_node = nr + dr, nc + dc
            if next_next_node in perimiter:
                q.append(next_node)
                outer_perimeter.add(next_node)
                visited.add(next_node)

for total, (r1, c1), (r2, c2) in tqdm(all_areas):
    corners = [(r1, c1), (r2, c1), (r2, c2), (r1, c2)]
    corners = corners + [corners[0]]
    valid = True
    for (r1, c1), (r2, c2) in zip(corners, corners[1:]):
        border = {(r,c) for r in range(min(r1, r2), max(r1, r2) + 1) for c in range(min(c1, c2), max(c1, c2) + 1)}
        if border & outer_perimeter:
            valid = False
            break
    if valid:
        print(total)
        break