from heapq import heappop, heappush
from collections import defaultdict

data = [l.strip() for l in open("data/23.test.in")]

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

q = [(*S,)]
visited = set(q)
graph = defaultdict(lambda: defaultdict(int))


while q:
    r, c = heappop(q)

    n_adjacent = 0
    for ndr, ndc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_r, next_c = r + ndr, c + ndc

        if next_r < 0 or next_r > len(data) - 1 or next_c < 0  or next_c > len(data[0]) - 1:  # fmt: skip
            continue

        if data[next_r][next_c] not in ".>v":
            continue

        next_node = (next_r, next_c)
        graph[(r, c)][next_node] = 1
        graph[next_node][(r, c)] = 1
        if next_node not in visited:
            heappush(q, next_node)
            visited.add(next_node)


intermediate_keys = {k for k, v in graph.items() if len(v) == 2}

for node in intermediate_keys:
    (n1, w1), (n2, w2) = graph[node].items()

    new_weight = w1 + w2

    graph[n1][n2] = new_weight
    graph[n2][n1] = new_weight

    graph[n1].pop(node)
    graph[n2].pop(node)
    graph.pop(node)

q = [(0, *S, [])]
visited = [(*S, [])]
P2 = 0
while q:
    pl, r, c, trace = heappop(q)

    if (r, c) == T:
        new_max = max(P2, -pl)
        if new_max > P2:
            P2 = new_max
            print(P2)

    for edge_k, edge_v in graph[(r, c)].items():
        next_node = (*edge_k, trace + [edge_k])

        if next_node not in visited and edge_k not in trace:
            visited.append(next_node)
            heappush(q, (pl - edge_v, *next_node))
print(P2)
