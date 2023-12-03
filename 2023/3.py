import re
from collections import namedtuple, defaultdict

digits = re.compile("[0-9]+")
chars = re.compile(r"[^a-zA-Z0-9\.]")
Point = namedtuple("Point", ["x", "y"])
dirs = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (-1, 0), (0, -1)]
data = [l.strip() for l in open("data/3.in")]

# Part 1
partnumbers = []
parts = set()
for i, l in enumerate(data):
    for d in digits.finditer(l):
        coords = [Point(y, i) for y in range(*d.span())]
        partnumbers.append((int(d.group()), coords))
    for p in chars.finditer(l):
        coords = [Point(y, i) for y in range(*p.span())]
        parts.add((p.group(), *coords))


found_parts = set()
for p, coords in partnumbers:
    for pos in coords:
        for dx, dy in dirs:
            if Point(pos.x + dx, pos.y + dy) in [pcoords for _, pcoords in parts]:
                found_parts.add((p, coords[0]))

print(sum((n for n, _ in found_parts)))

# Part 2
potential_gears = [p for p in parts if p[0] == "*"]

gears = defaultdict(set)
for p, coords in partnumbers:
    for pos in coords:
        for dx, dy in dirs:
            if Point(pos.x + dx, pos.y + dy) in [gc for _, gc in potential_gears]:
                gears[Point(pos.x + dx, pos.y + dy)].add(p)

total = 0
for g, p in gears.items():
    if len(p) == 2:
        p = list(p)
        total += p[0] * p[1]

print(total)
