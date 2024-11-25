#%%
# 
data = [int(l.strip()) for l in open('data/1.in')]

# %%
# Part 1 - count the number of increases

prev = 1e9
P1 = 0
for d in data:
    if d > prev:
        P1 += 1
    prev = d

print(P1)

# %%

prev = 1e9
P2 = 0
for d in zip(data[0:], data[1:], data[2:]):
    if sum(d) > prev:
        P2 += 1
    prev = sum(d)
print(P2)
# %%
