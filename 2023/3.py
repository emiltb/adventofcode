import re
from collections import namedtuple, defaultdict
import math

digits = re.compile("[0-9]+")
chars = re.compile(r"[^a-zA-Z0-9\.]")
Point = namedtuple("Point", ["x", "y"])
dirs = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (-1, 0), (0, -1)]
data = [l.strip() for l in open("data/3.in")]

# Part 1 and 2
partnumbers = []
parts = set()
for i, l in enumerate(data):
    for d in digits.finditer(l):
        coords = [Point(x, i) for x in range(*d.span())]
        partnumbers.append((int(d.group()), coords))
    for p in chars.finditer(l):
        coords = [Point(x, i) for x in range(*p.span())]
        parts.add((p.group(), *coords))


found_parts = set()
gears = defaultdict(set)
for p, coords in partnumbers:
    for pos in coords:
        for dx, dy in dirs:
            next_p = Point(pos.x + dx, pos.y + dy)
            if next_p in [pcoords for part, pcoords in parts]:
                found_parts.add((p, coords[0]))
            if next_p in [pcoords for part, pcoords in parts if part == "*"]:
                gears[next_p].add(p)

print(sum((n for n, _ in found_parts)))
print(sum(math.prod(p) for p in gears.values() if len(p) == 2))
