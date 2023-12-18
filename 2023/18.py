from collections import deque
data = [(d, int(l), c) for d, l, c in [l.strip().split() for l in open('data/18.in')]]

# Part 1
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

# Part 2
instructions = [(int("".join(n[:5]), 16),int(n[5:][0])) for n in [[s for s in d if s in '0123456789abcdef'] for _, _, d in data]]

trace = [(0,0)]
trace_len = 0
for l, d in instructions:
    match d:
        case 0: dr, dc = (0,1)
        case 1: dr, dc = (-1,0)
        case 2: dr, dc = (0,-1)
        case 3: dr, dc = (1,0)
    next_pos = (trace[-1][0] + dr * l, trace[-1][1] + dc * l)
    trace.append(next_pos)
    trace_len += l

# Shoelace formula
internal_area = 0
for i in range(len(trace) - 1):
    internal_area += (trace[i][0] * trace[i+1][1] - trace[i+1][0] * trace[i][1] )
internal_area = internal_area // 2


# Picks theorem
# A = I + b // 2 + 1
P2 = internal_area + trace_len // 2 + 1
print(P2)
