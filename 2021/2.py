#%%
data = [l.strip() for l in open('data/2.in')]


pos = (0,0)

for d in data:
    dir, l = d.split()
    if dir == "forward":
        pos = (pos[0] + int(l), pos[1])
    if dir == "up":
        pos = (pos[0], pos[1] - int(l))
    if dir == "down":
        pos = (pos[0], pos[1] + int(l))

print(pos[0] * pos[1])
# %%


pos = (0,0)
aim = 0

for d in data:
    dir, l = d.split()
    if dir == "forward":
        pos = (pos[0] + int(l), pos[1] + (aim * int(l)))
    if dir == "up":
        aim = aim - int(l)
    if dir == "down":
        aim = aim + int(l)

print(pos[0] * pos[1])

# %%
