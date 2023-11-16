import re


def merge_ranges(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    ranges = []
    # Insert first interval into stack
    ranges.append(intervals[0])
    for i in intervals[1:]:
        # If the next interval overlaps, modify the endpoint
        if ranges[-1][0] <= i[0] <= ranges[-1][-1]:
            ranges[-1][-1] = max(ranges[-1][-1], i[-1])
        else:
            ranges.append(i)

    return ranges


data = [
    [int(n) for n in re.findall("-?[\d]+", s)]
    for s in open("inputs/input15.txt").read().strip().splitlines()
]

sensors = [(a, b) for (a, b, *_) in data]
beacons = [(c, d) for (*_, c, d) in data]

y_target = 2000000

x_ranges = []
for s, b in zip(sensors, beacons):
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])

    min_y, max_y = s[1] - dist, s[1] + dist
    if min_y <= y_target <= max_y:
        dist_x = dist - abs(y_target - s[1])
        min_x, max_x = s[0] - dist_x, s[0] + dist_x
        x_ranges.append([min_x, max_x])

total_range = merge_ranges(x_ranges)

print(
    "In the row where y=2000000, how many positions cannot contain a beacon?",
    [r[1] - r[0] for r in total_range][0],
)

# Part 2
# Look for the beacon at all x and y from 0 to 4000000

lim = 4000000

for y in range(lim + 1):
    x_r = []

    for (sx, sy), (bx, by) in zip(sensors, beacons):
        dist = abs(sx - bx) + abs(sy - by)
        dist_x = dist - abs(y - sy)

        if dist_x < 0:
            continue

        min_x, max_x = sx - dist_x, sx + dist_x

        x_r.append([min_x, max_x])

    x_r = merge_ranges(x_r)

    x = 0
    for lo, hi in x_r:
        if x < lo:
            print(f"Beacon at x={x}, y={y}")
            print("What is its tuning frequency?", x * 4000000 + y)
            break
        x = max(x, hi + 1)
        if x > lim:
            break
