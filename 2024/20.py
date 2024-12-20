from collections import Counter, defaultdict
data = [l.strip() for l in open('data/20.in')]
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

print(sum(v for k, v in Counter(P1).items() if k >= 100))
