from collections import deque
from itertools import combinations

data = [l.strip() for l in open("data/16.in")]

grid = dict()
for r, l in enumerate(data):
    for c, d in enumerate(l):
        grid[(r, c)] = d


# Part 1
def f(S):
    q = deque([S])
    visited = {q[0]}

    while q:
        (r, c), (dr, dc) = q.popleft()
        match grid[(r, c)]:
            case ".":
                next_pos = [(r + dr, c + dc)]
                next_dir = [(dr, dc)]
            case "|":
                if (dr, dc) == (0, 1) or (dr, dc) == (0, -1):
                    next_pos = [(r - 1, c), (r + 1, c)]
                    next_dir = [(-1, 0), (1, 0)]
                if (dr, dc) == (1, 0) or (dr, dc) == (-1, 0):
                    next_pos = [(r + dr, c + dc)]
                    next_dir = [(dr, dc)]
            case "-":
                if (dr, dc) == (1, 0) or (dr, dc) == (-1, 0):
                    next_pos = [(r, c - 1), (r, c + 1)]
                    next_dir = [(0, -1), (0, 1)]
                if (dr, dc) == (0, 1) or (dr, dc) == (0, -1):
                    next_pos = [(r + dr, c + dc)]
                    next_dir = [(dr, dc)]
            case "/":
                if (dr, dc) == (1, 0):
                    next_pos = [(r, c - 1)]
                    next_dir = [(0, -1)]
                if (dr, dc) == (-1, 0):
                    next_pos = [(r, c + 1)]
                    next_dir = [(0, 1)]
                if (dr, dc) == (0, 1):
                    next_pos = [(r - 1, c)]
                    next_dir = [(-1, 0)]
                if (dr, dc) == (0, -1):
                    next_pos = [(r + 1, c)]
                    next_dir = [(1, 0)]
            case "\\":
                if (dr, dc) == (1, 0):
                    next_pos = [(r, c + 1)]
                    next_dir = [(0, 1)]
                if (dr, dc) == (-1, 0):
                    next_pos = [(r, c - 1)]
                    next_dir = [(0, -1)]
                if (dr, dc) == (0, 1):
                    next_pos = [(r + 1, c)]
                    next_dir = [(1, 0)]
                if (dr, dc) == (0, -1):
                    next_pos = [(r - 1, c)]
                    next_dir = [(-1, 0)]

        for p, d in zip(next_pos, next_dir):
            if p in grid and (p, d) not in visited:
                q.append((p, d))
                visited.add((p, d))

    return len({p for p, _ in visited})


P1 = f(((0, 0), (0, 1)))
print(P1)

# Part 2
P2 = 0
for kr, kc in grid:
    if kr == 0:
        start = ((kr, kc), (1, 0))
    elif kr == len(data) - 1:
        start = ((kr, kc), (-1, 0))
    elif kc == 0:
        start = ((kr, kc), (0, 1))
    elif kc == len(data) - 1:
        start = ((kr, kc), (0, -1))
    else:
        start = None

    if start:
        P2 = max(P2, f(start))
print(P2)
