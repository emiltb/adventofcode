from collections import deque

voxels = {
    tuple([int(n) for n in v.strip().split(",")])
    for v in open("inputs/input18.txt").readlines()
}

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

s = 0
# Check all voxels
for x, y, z in voxels:
    # Examine all immediate neighbours.
    for dx, dy, dz in dirs:
        # If the neighbour does not exist it contributes to
        # surface area
        if (x + dx, y + dy, z + dz) not in voxels:
            s += 1
print("Surface area of obsidian:", s)

# Part 2

# Set outer bounds that we are sure are outside the obsidian
def minmax(l):
    return min(l) - 1, max(l) + 1


min_x, max_x = minmax([x for (x, y, z) in voxels])
min_y, max_y = minmax([y for (x, y, z) in voxels])
min_z, max_z = minmax([z for (x, y, z) in voxels])

# Inititate in the lowest corner
faces = 0
visited = set((min_x, min_y, min_z))

# Set up a queue of points to visit
q = deque([(min_x, min_y, min_z)])

# While there are still items in the queue
while q:
    # Pick the next item
    x, y, z = q.popleft()

    # Check all neighbours
    for dx, dy, dz in dirs:
        # Set coordinates of neighbour
        nx, ny, nz = k = (x + dx, y + dy, z + dz)

        # If we are outside the outer bounds
        if not (min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z):
            continue

        # If the neighbour is part of the obsidian
        if k in voxels:
            faces += 1
            continue

        # If we have already visited the neighbour
        if k in visited:
            continue

        # Otherwise add the neighbour to the queue and mark it as visited
        q.append(k)
        visited.add(k)

print("Outer surface of obsidian:", faces)
