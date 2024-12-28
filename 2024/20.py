from collections import Counter, defaultdict, deque
data = [l.strip() for l in open('data/20.test.in')]
grid = {(r,c) for r, l in enumerate(data) for c, s in enumerate(l) if s == '#'}
start = [(r,c) for r, l in enumerate(data) for c, s in enumerate(l) if s == 'S'][0]

rows = len(data)
cols = len(data[0])

q = [(0, *start)]
visited = defaultdict(lambda: None)
visited[start] = 0

while q:
    steps, r, c = q.pop()

    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if (nr, nc) in grid or visited[(nr, nc)] is not None:
            continue

        q.append((steps + 1, nr, nc))
        visited[(nr, nc)] = steps + 1

P1 = []
inner_grid = {(r,c) for r, c in grid if r not in (0, rows-1) and c not in (0, cols-1)}
for r, c in inner_grid:
    neighbors = list({(r + dr, c + dc) for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]} & visited.keys())
    if len(neighbors) == 2:
        n1, n2 = neighbors
        P1.append(abs(visited[n1] - visited[n2]) - 2)

print(sum(v for k, v in Counter(P1).items() if k >= 50))


cheats = {}
for pos in visited:
    print(f"Check cheats starting at {pos}")

    q = deque([(0, *pos)])
    cheat_visisted = set()

    while q:
        steps, r, c = q.popleft()

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (nr, nc) in visited and visited[(nr,nc)] > visited[pos] and (pos,(nr,nc)) not in cheats:
                cheats[pos,(nr,nc)] = visited[(nr,nc)] - visited[pos] - steps - 1
                continue

            if (nr, nc) not in inner_grid or (nr,nc) in cheat_visisted or steps >= 20:
                continue

            q.append((steps + 1, nr, nc))
            cheat_visisted.add((nr, nc))

print({(start, end): s for (start, end), s in cheats.items() if start == (3,1)})
# print({k: v for k, v in cheats.items() if v >= 70})
print(sum(v for k, v in Counter(cheats.values()).items() if k >= 70))
# print(Counter(cheats.values()))