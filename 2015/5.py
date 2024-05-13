# %% 
import re
data = [l.strip() for l in open('data/5.in')]

# %% Part 1
P1 = 0
for s in data:
    c1 = len(re.findall('[aeiou]', s)) >= 3
    c2 = re.search(r"(.)\1", s)
    c3 = re.search(r"ab|cd|pq|xy", s)
    if c1 and c2 and not c3:
        P1 += 1

print(P1)

# %%
P2 = 0
for s in data:
    c1 = re.search(r"([a-z]{2})(.)*\1", s)
    c2 = re.search(r"([a-z]{1})([a-z]){1}\1", s)
    if c1 and c2:
        P2 += 1

print(P2)
# %%
