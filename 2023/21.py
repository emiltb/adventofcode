from collections import deque

data = [l.strip() for l in open("data/21.in")]

S = [(0, r, c) for r, l in enumerate(data) for c, s in enumerate(l) if s == "S"]

P1 = set()
visited = set()
q = deque(S)
while q:
    n, r, c = q.popleft()
    if n == 64:
        P1.add((r, c))
        continue
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_r, next_c = r + dr, c + dc
        if data[next_r][next_c] != "#":
            next_node = (n + 1, next_r, next_c)
            if next_node not in visited:
                q.append(next_node)
                visited.add(next_node)

print(len(P1))
