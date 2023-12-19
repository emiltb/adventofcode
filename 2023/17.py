from collections import namedtuple
from heapq import heappop, heappush

data = [l.strip() for l in open("data/17.in")]

block = namedtuple("block", ["heatloss", "r", "c", "dr", "dc", "n"])

# Part 1
S = block(0, 0, 0, 0, 0, 0)
T = (len(data) - 1, len(data[0]) - 1)
q = [S]
visited = set()

while q:
    node = heappop(q)

    if (node.r, node.c) == T:
        print(node.heatloss)
        break

    if (node.r, node.c, node.dr, node.dc, node.n) in visited:
        continue

    visited.add((node.r, node.c, node.dr, node.dc, node.n))

    for ndr, ndc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_r, next_c = node.r + ndr, node.c + ndc
        if next_r < 0 or next_r > len(data) - 1 or next_c < 0  or next_c > len(data[0]) - 1:  # fmt: skip
            continue

        if (ndr, ndc) == (-node.dr, -node.dc):
            continue

        n = 1 if (ndr, ndc) != (node.dr, node.dc) else node.n + 1
        if n > 3:
            continue

        heappush(q, block(node.heatloss + int(data[next_r][next_c]), next_r, next_c, ndr, ndc, n))  # fmt: skip

# Part 2
q = [S]
visited = set()

while q:
    node = heappop(q)

    if (node.r, node.c) == T:
        print(node.heatloss)
        break

    for ndr, ndc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        next_r, next_c = node.r + ndr, node.c + ndc
        if next_r < 0 or next_r > len(data) - 1 or next_c < 0  or next_c > len(data[0]) - 1:  # fmt: skip
            continue

        if (ndr, ndc) == (-node.dr, -node.dc):
            continue

        n = 1 if (ndr, ndc) != (node.dr, node.dc) else node.n + 1

        if n > 10:
            continue

        if (next_r, next_c, ndr, ndc, n) in visited:
                continue

        if node.n >= 4 or (node.dr, node.dc) == (0,0) or (ndr, ndc) == (node.dr, node.dc):
            heappush(q, block(node.heatloss + int(data[next_r][next_c]), next_r, next_c, ndr, ndc, n))  # fmt: skip
            visited.add((next_r, next_c, ndr, ndc, n))
