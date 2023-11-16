from collections import deque


tunnels = {}
valves = {}
with open("inputs/input16.txt", "r") as f:
    for l in f:
        line = [p.split() for p in l.split(";")]
        tunnels[line[0][1]] = [n.strip(",") for n in line[1][4:]]
        valves[line[0][1]] = int(line[0][-1].split("=")[-1])

distances = {}
nonempty = []

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        nonempty.append(valve)

    distances[valve] = {valve: 0, "AA": 0}
    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbour in tunnels[position]:
            if neighbour in visited:
                continue
            visited.add(neighbour)
            if valves[neighbour]:
                distances[valve][neighbour] = distance + 1
            queue.append((distance + 1, neighbour))

    del distances[valve][valve]
    if valve != "AA":
        del distances[valve]["AA"]

indices = {}

for index, element in enumerate(nonempty):
    indices[element] = index

indices

cache = {}


def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    maxval = 0
    for neighbor in distances[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue
        remtime = time - distances[valve][neighbor] - 1
        if remtime <= 0:
            continue
        maxval = max(
            maxval, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime
        )

    cache[(time, valve, bitmask)] = maxval
    return maxval


print(dfs(30, "AA", 0))
