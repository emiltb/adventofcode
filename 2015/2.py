# %%
data = [sorted([int(n) for n in l.strip().split('x')]) for l in open('data/2.in')]

# %% Part 1
area = sum(2*(x*y + x*z + y*z) + x*y for x, y, z in data)
print(area)

# %% Part 2
length = sum(2*x + 2*y + x*y*z for x, y, z in data)
print(length)
