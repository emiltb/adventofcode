from collections import deque
data = [l.strip() for l in open('data/12.in')]

grid = {(r,c): s for r, l in enumerate(data) for c, s in enumerate(l)}
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
areas = []

q = deque([(0,0)])
visited = set([q[0]])

P1 = 0
perim = 0
perims = []
region = []
while q:
    r, c = q.popleft()
    region.append((r, c))
    visited.add((r, c))
    print(r,c)

    for dr, dc in dirs:
        next_r, next_c = r + dr, c + dc

        if (next_r, next_c) not in grid.keys() or grid[(r,c)] != grid[(next_r, next_c)]:
            perim += 1
            continue

        if (next_r, next_c) in visited or (next_r, next_c) in q:
            continue

        q.append((next_r, next_c))

    if len(q) == 0 and len(visited) != len(grid):
        perims.append(perim)
        perim = 0
        areas.append(region)
        region = []
        next_pos = ((r,c) for r, c in grid.keys() if (r,c) not in visited)
        next_r, next_c = next(next_pos)
        q.append((next_r, next_c))

areas.append(region)
perims.append(perim)
for a in areas:
    print(a)
print([len(l) for l in areas])
print(perims)
print(len(areas))
print(len(perims))

print(sum(len(r)*p for r, p in zip(areas, perims)))