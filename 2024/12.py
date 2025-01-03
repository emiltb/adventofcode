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
    side = defaultdict(list)
    for r in range(r_min, r_max + 1):
        for c in range(c_min, c_max + 1):
            for bound, (cr, cc) in zip(['upper','lower'], [(r - 1, c), (r + 1, c)]):
                if (cr, cc) not in area and (r,c) in area:
                    side[bound].append((r,c))
                elif side[bound]:
                        sides.append(side[bound])
                        side[bound] = []

        for bound in ['upper','lower']:
            if side[bound]:
                sides.append(side[bound])
                side[bound] = []

    for c in range(c_min, c_max + 1):
        for r in range(r_min, r_max + 1):
            for bound, (cr, cc) in zip(['left','right'], [(r, c - 1), (r, c + 1)]):
                if (cr, cc) not in area and (r,c) in area:
                    side[bound].append((r,c))
                elif side[bound]:
                        sides.append(side[bound])
                        side[bound] = []

        for bound in ['left','right']:
            if side[bound]:
                sides.append(side[bound])
                side[bound] = []    

    return len(area) * len(sides)


print(sum(calculate_price(a) for a in areas.values()))


def count_corners(area):
    corners = set()
    for r, c in area:
        for nr, nc in [(r - 0.5, c - 0.5),(r - 0.5, c + 0.5), (r + 0.5, c + 0.5), (r + 0.5, c - 0.5)]:
            corners.add((nr, nc))
    
    n_corners = 0
    for r, c in corners:
        neighbours = [(nr, nc) in area for nr, nc in [(r - 0.5, c - 0.5),(r - 0.5, c + 0.5), (r + 0.5, c + 0.5), (r + 0.5, c - 0.5)]]

        if sum(neighbours) == 3: n_corners += 1
        if sum(neighbours) == 1: n_corners += 1
        if sum(neighbours) == 2:
            if neighbours == [True, False, True, False] or neighbours == [False, True, False, True]:
                n_corners += 2

    return len(area)*n_corners

print(sum(count_corners(a) for a in areas.values()))
