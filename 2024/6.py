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
for rb, cb in visited.copy():
    dirs = deque([(-1,0),(0,1),(1,0),(0,-1)])
    pos = (*start, dirs[0])
    visited = set([pos])

    while 0 < pos[0] < len(data)-1 and 0 < pos[1] < len(data[0])-1:
        d = dirs[0]
        next_r, next_c = pos[0] + d[0], pos[1] + d[1]
        if data[next_r][next_c] != "#" and (next_r,next_c) != (rb, cb):
            pos = (next_r, next_c, d)
            if pos in visited:
                p2 += 1
                break
            visited.add(pos)
        else:
            dirs.rotate(-1)
    
print(p2)