from heapq import heappop, heappush

grid = {(r,c): s for r, l in enumerate(open('data/16.in').readlines()) for c, s in enumerate(l.strip())}

start = [(r,c) for (r,c), s in grid.items() if s == 'S'][0]
end = [(r,c) for (r,c), s in grid.items() if s == 'E'][0]
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
dir = dirs[0]

q = [(0, *start, *dir, set([start]))]
visited = set()
min_points = 1e9
best_paths = set()
while q:
    points, r, c, pdr, pdc, trace = heappop(q)
    visited.add((r, c, pdr, pdc) )
    if (r,c) == end:
        if points <= min_points:
            best_paths |= set(trace)
            min_points = min(min_points, points)

    for dr, dc in [(dr, dc) for dr, dc in dirs if (dr != -pdr and dc != -pdc) or (dr, dc) == (pdr, pdc)]:
        next_r, next_c = r + dr, c + dc

        if grid[(next_r, next_c)] == '#' or (next_r, next_c) in trace or (next_r, next_c, dr, dc) in visited:
            continue

        next_points = points
        if (pdr, pdc) != (dr, dc): 
            next_points += 1000

        next_node = (next_points + 1, next_r, next_c, dr, dc, trace | set([(next_r, next_c)]))
        heappush(q, next_node)

print(min_points)
print(len(best_paths))