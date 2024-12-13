from collections import deque, defaultdict
data = [l.strip() for l in open('data/12.in')]

grid = {(r,c): s for r, l in enumerate(data) for c, s in enumerate(l)}
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

q = deque([list(grid)[0]])
visited = set([q[0]])
areas = defaultdict(list)
perims = defaultdict(list)
i = 0
while q:
    r, c = q.popleft()
    areas[i].append((r, c))
    visited.add((r, c))

    for dr, dc in dirs:
        next_pos = r + dr, c + dc

        if next_pos not in grid or grid[(r,c)] != grid[next_pos]:
            perims[i].append((r,c))
            continue
        if next_pos in visited or next_pos in q:
            continue

        q.append(next_pos)

    if len(q) == 0 and (next_pos := [(r,c) for r, c in grid if (r,c) not in visited]):
        q.append((*next_pos[0],))
        i += 1

print(sum(len(a)*len(p) for a, p in zip(areas.values(), perims.values())))


def calculate_price(area):
    r_min, r_max = min([r for r, _ in area]), max([r for r, _ in area])
    c_min, c_max = min([c for _, c in area]), max([c for _, c in area])
    sides = []
    side_upper = []
    side_lower = []
    for r in range(r_min, r_max + 1):
        for c in range(c_min, c_max + 1):
            if (r - 1, c) not in area and (r,c) in area:
                side_upper.append((r,c, 'up'))
            else:
                if side_upper:
                    sides.append(side_upper)
                    side_upper = []

            if (r + 1, c) not in area and (r,c) in area:
                side_lower.append((r,c, 'lo'))
            else:
                if side_lower:
                    sides.append(side_lower)
                    side_lower = []

        if side_upper:
            sides.append(side_upper)
            side_upper = []
        if side_lower:
            sides.append(side_lower)
            side_lower = []

    side_left = []
    side_right = []
    for c in range(c_min, c_max + 1):
        for r in range(r_min, r_max + 1):
            if (r, c - 1) not in area and (r,c) in area:
                side_left.append((r,c, 'le'))
            else:
                if side_left:
                    sides.append(side_left)
                    side_left = []

            if (r, c + 1) not in area and (r,c) in area:
                side_right.append((r,c, 'ri'))
            else:
                if side_right:
                    sides.append(side_right)
                    side_right = []
        if side_left:
                    sides.append(side_left)
                    side_left = []
        if side_right:
                sides.append(side_right)
                side_right = []     

    return len(area) * len(sides)


print(sum(calculate_price(a) for a in areas.values()))
print(areas[0])