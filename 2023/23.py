from heapq import heappop, heappush

data = [l.strip() for l in open("data/23.in")]

# Part 1
S = [(0, c) for c, s in enumerate(data[0]) if s == "."][0]
T = [(len(data) - 1, c) for c, s in enumerate(data[-1]) if s == "."][0]

q = [(0, *S, 0, 0)]
visited = set(q)

P1 = 0
while q:
    steps, r, c, dr, dc = heappop(q)

    if (r, c) == T:
        P1 = max(steps, P1)

    for ndr, ndc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_r, next_c = r + ndr, c + ndc

        if (dr, dc) == (-ndr, -ndc):
            continue

        if next_r < 0 or next_r > len(data) - 1 or next_c < 0  or next_c > len(data[0]) - 1:  # fmt: skip
            continue

        if data[next_r][next_c] not in ".>v":
            continue

        if (data[next_r][next_c] == "v" and (ndr, ndc) != (1, 0)) or (data[next_r][next_c] == ">" and (ndr, ndc) != (0, 1)):  # fmt: skip
            continue

        next_node = (steps + 1, next_r, next_c, ndr, ndc)
        if next_node not in visited:
            heappush(q, next_node)
            visited.add(next_node)

print(P1)

# Part 2

q = [(0, *S, 0, 0, [])]
visited = [q[0]]

P2 = 0
while q:
    steps, r, c, dr, dc, trace = heappop(q)
    # print(steps, r, c, dr, dc, trace)

    if (r, c) == T:
        P2 = max(-steps, P2)
        print(P2)
        continue

    for ndr, ndc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_r, next_c = r + ndr, c + ndc

        if (dr, dc) == (-ndr, -ndc):
            continue

        if next_r < 0 or next_r > len(data) - 1 or next_c < 0  or next_c > len(data[0]) - 1:  # fmt: skip
            continue

        if data[next_r][next_c] not in ".>v":
            continue

        next_node = (steps - 1, next_r, next_c, ndr, ndc, trace + [(next_r, next_c)])
        if next_node not in visited and (next_r, next_c) not in trace:
            heappush(q, next_node)
            visited.append(next_node)

print(P2)
