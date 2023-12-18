from collections import deque
data = [(d, int(l), c) for d, l, c in [l.strip().split() for l in open('data/18.in')]]

trace = [(0,0)]

for d, l, _ in data:
    match d:
        case "R": dr, dc = (0,1)
        case "L": dr, dc = (0,-1)
        case "U": dr, dc = (1,0)
        case "D": dr, dc = (-1,0)
    for i in range(l):
        next_pos = (trace[-1][0] + dr, trace[-1][1] + dc)
        trace.append(next_pos)

P1 = len(trace) - 1
q = deque([(-1,1)])
visited = set()
while q:
    r, c = q.popleft()

    if (r,c) in visited:
        continue
    visited.add((r,c))
    P1 += 1

    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r + dr, c + dc
        if (nr,nc) in trace:
            continue
        q.append((nr,nc))

print(P1)
