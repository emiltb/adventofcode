from collections import deque, defaultdict
from pprint import pprint

data = [l.strip() for l in open("data/17.test.in")]

data

S = (0, 0, 0, 0)
T = (len(data) - 1, len(data[0]) - 1)

q = deque([S])
visited = defaultdict(lambda: 1e6)
visited[S] = 0
steps = defaultdict(list)
trace = defaultdict(list)
next_heat_loss = 0
while q:
    r, c, pdr, pdc = q.popleft()
    # print(r, c, dr, pdc)

    if (r, c) == T:
        print(next_heat_loss)
        break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_r, next_c = r + dr, c + dc
        if next_r < 0 or next_r > len(data) - 1 or next_c < 0  or next_c > len(data[0]) - 1:  # fmt: skip
            continue

        # print(next_r, next_c)

        if all(s == (dr, dc) for s in steps[(r, c)][-3:]) and len(steps[(r, c)]) >= 3:
            # print("Repeating too many steps")
            # print((r, c), steps[(r, c)], (dr, dc))
            continue
        # print(next_r, next_c, data[next_r][next_c])

        next_heat_loss = visited[(r, c, pdr, pdc)] + int(data[next_r][next_c])
        # print(next_heat_loss)
        if next_heat_loss <= visited[(next_r, next_c, dr, dc)]:
            q.append((next_r, next_c, dr, dc))
            visited[((next_r, next_c, dr, dc))] = next_heat_loss
            steps[((next_r, next_c, dr, dc))] = steps[(r, c)] + [(dr, dc)]
            trace[((next_r, next_c))] = trace[(r, c)] + [(next_r, next_c)]

print(visited[T])


for r, l in enumerate(data):
    for c, d in enumerate(l):
        if (r, c) in trace[T]:
            print(".", end="")
        else:
            print(d, end="")
    print()

pprint(data)
trace[T]
