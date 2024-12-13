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
# print(perims[i])
# print(areas[i])
# print(set(areas[i]))

def print_region(d, p):
    r_min, r_max = min([r for r, _ in d]), max([r for r, _ in d])
    c_min, c_max = min([c for _, c in d]), max([c for _, c in d])
    print(r_min, r_max, c_min, c_max)
    for r in range(r_min - 1, r_max + 2):
        for c in range(c_min - 1, c_max + 2):
            char = '.'
            if (r,c) in d: char = "#"
            if (r,c) in p: char = "X"
            print(char, end="")
        print()

i = 239
print(len(areas[i]),len(set(areas[i])))
print(len(perims[i]),len(set(perims[i])))
print_region(areas[i], perims[i])
# for i in range(len(areas)):
#     print(f"i: {i}")
#     print_region(areas[i], perims[i])
#     print()