from collections import deque, defaultdict
data = [l.strip() for l in open('data/12.in')]

grid = {(r,c): s for r, l in enumerate(data) for c, s in enumerate(l)}
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

q = deque([(0,0)])
visited = set([q[0]])

areas = defaultdict(list)
perims = defaultdict(int)
i = 0
while q:
    r, c = q.popleft()
    areas[i].append((r, c))
    visited.add((r, c))

    for dr, dc in dirs:
        next_pos = r + dr, c + dc

        if next_pos not in grid.keys() or grid[(r,c)] != grid[next_pos]:
            perims[i] += 1
            continue

        if next_pos in visited or next_pos in q:
            continue

        q.append(next_pos)

    if len(q) == 0 and (next_pos := [(r,c) for r, c in grid.keys() if (r,c) not in visited]):
        q.append((*next_pos[0],))
        i += 1

print(sum(len(a)*p for a, p in zip(areas.values(), perims.values())))