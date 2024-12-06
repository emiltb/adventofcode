from collections import deque
data = [l.strip() for l in open('data/6.in')]

pos = [(r, c) for r, l in enumerate(data) for c, s in enumerate(l) if s == '^'][0]
dirs = deque([(-1,0),(0,1),(1,0),(0,-1)])
visited = set([pos])

while 0 < pos[0] < len(data)-1 and 0 < pos[1] < len(data[0])-1:
    d = dirs[0]
    if data[pos[0] + d[0]][pos[1] + d[1]] != "#":
        pos = (pos[0] + d[0], pos[1] + d[1])
        visited.add(pos)
    else:
        dirs.rotate(-1)
print(len(visited))