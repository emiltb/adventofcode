from collections import deque, defaultdict
import numpy as np

data = [l.strip() for l in open("data/21.in")]
steps = 26501365

assert len(data) == len(data[0])
size = len(data)

S = [(0, r, c) for r, l in enumerate(data) for c, s in enumerate(l) if s == "S"]

P2_params = []
visited = set()
q = deque(S)
P1_max = 0
P2_max = 0
while q:
    nn = q[0][0]
    if nn > P1_max:
        if nn == 64:
            print(len(q))
        P1_max = nn

    if nn % size == size // 2 and nn > P2_max:
        P2_max = nn
        P2_params.append(len(q))

    n, r, c = q.popleft()

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_r, next_c = r + dr, c + dc
        if data[next_r % size][next_c % size] != "#":
            next_node = (n + 1, next_r, next_c)
            if next_node not in visited and n + 1 <= size * 3:
                q.append(next_node)
                visited.add(next_node)

# Part 2
fit = np.array(np.polyfit([0,1,2], P2_params, 2), dtype=np.int64)
grid_size = steps // size
print(fit[0] * grid_size ** 2 + fit[1] * grid_size + fit[2])
