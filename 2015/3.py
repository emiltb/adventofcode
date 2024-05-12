# %%
data = [l.strip() for l in open('data/3.in')][0]

# %%
dirs = {'^': (0,1), 'v': (0,-1), '>': (1,0), '<': (-1,0)}
pos = (0,0)
visited = set([pos])

for s in data:
    n = dirs[s]
    pos = (pos[0] + n[0], pos[1] + n[1])
    visited.add(pos)
print(len(visited))

# %%
visited = set([(0,0)])

for l in [data[::2], data[1::2]]:
    pos = (0,0)
    for s in l:
        n = dirs[s]
        pos = (pos[0] + n[0], pos[1] + n[1])
        visited.add(pos)
print(len(visited))