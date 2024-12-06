from collections import deque
from copy import deepcopy
data = [l.strip() for l in open('data/6.in')]

start = pos = [(r, c) for r, l in enumerate(data) for c, s in enumerate(l) if s == '^'][0]
visited = set([pos])
dirs = deque([(-1,0),(0,1),(1,0),(0,-1)])

while 0 < pos[0] < len(data)-1 and 0 < pos[1] < len(data[0])-1:
    d = dirs[0]
    if data[pos[0] + d[0]][pos[1] + d[1]] != "#":
        pos = (pos[0] + d[0], pos[1] + d[1])
        visited.add(pos)
    else:
        dirs.rotate(-1)
print(len(visited))

p2 = 0
for rb, cb in ((r,c) for r in range(len(data)) for c in range(len(data[0]))):
    if data[rb][cb] == '#' or (rb,cb) == start:
        continue
    this_data = deepcopy(data)
    this_data[rb] = data[rb][:cb] + '#' + data[rb][cb + 1:]

    dirs = deque([(-1,0),(0,1),(1,0),(0,-1)])
    pos = (*start, dirs[0])
    visited = set([pos])

    while 0 < pos[0] < len(data)-1 and 0 < pos[1] < len(data[0])-1:
        d = dirs[0]
        if this_data[pos[0] + d[0]][pos[1] + d[1]] != "#":
            pos = (pos[0] + d[0], pos[1] + d[1], d)
            if pos in visited:
                p2 += 1
                break
            visited.add(pos)
        else:
            dirs.rotate(-1)
    
print(p2)