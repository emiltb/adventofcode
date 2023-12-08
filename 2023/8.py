import re
from collections import deque
from math import lcm

directions, *other = [l.strip() for l in open('data/8.in')]

# Part 1
dirs = deque(directions)
data = {k: (l, r) for k, l, r in [re.findall("[A-Z0-9]{3}",d) for d in other[1:]]}

P1 = 0
next_key = 'AAA'
while next_key != 'ZZZ':
    next_key = data[next_key][0 if dirs[0] == 'L' else 1]
    P1 += 1
    dirs.rotate(-1)
print(P1)

# Part 2
def find_z(next_key):
    dirs = deque(directions)
    c = 0
    while not next_key.endswith('Z'):
        next_key = data[next_key][0 if dirs[0] == 'L' else 1]
        c += 1
        dirs.rotate(-1)
    return c

P2 = []
for key in [k for k in data.keys() if k.endswith('A')]:
    P2.append(find_z(key))
print(lcm(*P2))
