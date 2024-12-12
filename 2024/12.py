from collections import deque, defaultdict
data = [l.strip() for l in open('data/12.in')]

grid = {(r,c): s for r, l in enumerate(data) for c, s in enumerate(l)}
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

q = deque([(0,0)])
visited = set([q[0]])

P1 = 0
perim = 0
perims = []
region = []
regions = []
while q:
    r, c = q.popleft()
    region.append((r, c))
    visited.add((r, c))

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
        regions.append(region)
        perim = 0
        region = []
        
        next_pos = ((r,c) for r, c in grid.keys() if (r,c) not in visited)
        next_r, next_c = next(next_pos)
        q.append((next_r, next_c))
else: 
    perims.append(perim)
    regions.append(region)

print(sum(len(r)*p for r, p in zip(regions, perims)))