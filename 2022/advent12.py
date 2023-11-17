# Failed to solve this one.
# Adapted from https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day12p1.py
from collections import deque
import matplotlib.pyplot as plt
from copy import deepcopy
import numpy as np

with open("inputs/input12.txt", "r") as f:
    raw_data = f.read()

grid = [s.strip().splitlines() for s in raw_data]
grid = [list(x) for x in open("inputs/input12.txt").read().strip().splitlines()]
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if item == "S":
            sr = r
            sc = c
            grid[r][c] = "a"
        if item == "E":
            er = r
            ec = c
            grid[r][c] = "z"

# Create the queue
queue = deque()

# Add the starting node as the first item in the queue
queue.append((0, sr, sc))

# Add the starting node as the first visited node
vis = {(sr, sc)}
node_map = deepcopy(grid)
node_map = np.zeros((len(grid), len(grid[0])))
node_map[sr, sc] = 0

while queue:
    # Visit the next node
    d, r, c = queue.popleft()

    # Check all the neighbours of the current node
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        # Check if it is a valid neighbour
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        # Check if the node has been visited before
        if (nr, nc) in vis:
            continue
        # Check if the height difference is too large
        if ord(grid[nr][nc]) - ord(grid[r][c]) > 1:
            continue
        # Check if it is the final node
        if nr == er and nc == ec:
            print(d + 1)
        # Add to visited nodes
        vis.add((nr, nc))
        queue.append((d + 1, nr, nc))
        node_map[nr, nc] = d + 1

fig = plt.figure()
ax = plt.axes()
ax.imshow(node_map)

# Part 2


# Create the queue
queue = deque()

# Add the starting node as the first item in the queue
queue.append((0, er, ec))

# Add the starting node as the first visited node
vis = {(er, ec)}
node_map = deepcopy(grid)
node_map = np.zeros((len(grid), len(grid[0]))) + 999
node_map[er, ec] = 0

while queue:
    # Visit the next node
    d, r, c = queue.popleft()
    node_map[r, c] = d

    # Check all the neighbours of the current node
    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        # Check if it is a valid neighbour
        if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
            continue
        # Check if the node has been visited before
        if (nr, nc) in vis:
            continue
        # Check if the height difference is too large - note that this is
        # different than the first part since we are tracking the path in reverse
        if ord(grid[nr][nc]) - ord(grid[r][c]) < -1:
            continue
        # Add to visited nodes
        vis.add((nr, nc))
        queue.append((d + 1, nr, nc))


fig = plt.figure()
ax = plt.axes()
ax.imshow(node_map)

np.where(np.array(grid) == "a")
a_list = []
for r, row in enumerate(grid):
    for c, item in enumerate(row):
        if grid[r][c] == "a":
            a_list.append(node_map[r, c])


min(a_list)
