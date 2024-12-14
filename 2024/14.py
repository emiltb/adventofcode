import re
from collections import Counter
data = [[int(n) for n in re.findall(r'(-?\d+)', l)] for l in open('data/14.in')]

robots = {i: {"p": (c,r), "v": (vc, vr)} for i, (r, c, vr, vc) in enumerate(data)}
bounds = (0, 103, 0, 101)

quadrants = [[(r, c) for r in range(0, bounds[1]//2) for c in range(0, bounds[3]//2)],
             [(r, c) for r in range(0, bounds[1]//2) for c in range(bounds[3]//2 + 1, bounds[3])],
             [(r, c) for r in range(bounds[1]//2 + 1, bounds[1]) for c in range(0, bounds[3]//2)],
             [(r, c) for r in range(bounds[1]//2 + 1, bounds[1]) for c in range(bounds[3]//2 + 1, bounds[3])]
            ]

def print_robots():
    for r in range(bounds[0], bounds[1]):
        for c in range(bounds[2], bounds[3]):
            n_robots = len([ro for ro in robots.values() if ro["p"] == (r, c)])
            if n_robots == 0:
                print('.', end="")
            else:
                print(n_robots, end="")
        print()

for s in range(1, 10000):
    for i in range(len(robots)):
        r, c = robots[i]["p"]
        vr, vc = robots[i]["v"]
        robots[i]["p"] = ((r + vr) % bounds[1], (c + vc) % bounds[3])
    if s == 100:
        P1 = 1
        q_count = Counter([i for r in robots.values() for i, q in enumerate(quadrants) if r["p"] in q])
        for c in q_count.values():
            P1 *= c
        print(P1)
    if (s % 101 == 68 and s % 103 == 31): # Offsets deduced from looking at prints of the robot layout
        print(f"s = {s}:")
        print_robots()
