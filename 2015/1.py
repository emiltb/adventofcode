# %%
data = [l.strip() for l in open('data/1.in')][0]

# %% Part 1
print(data.count('(') - data.count(')'))

# %% Part 2
floor = 0
for i, s in enumerate(data):
    floor = floor + 1 if s == '(' else floor - 1
    if floor == -1:
        print(i + 1)
        break
