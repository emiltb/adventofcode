# %%
from hashlib import md5
from itertools import count
data = [l.strip() for l in open('data/4.in')][0]

# %% Part 1 and 2
p1 = p2 = None
for i in count():
    s = data + str(i)
    hash = md5(s.encode()).hexdigest()
    if hash[:5] == '00000' and not p1:
        p1 = i
    if hash[:6] == '000000':
        p2 = i
        break
print(p1)
print(p2)