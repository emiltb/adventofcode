# %% 
import re
data = [l.strip() for l in open('data/5.in')]

# %% Part 1
P1 = 0
for s in data:
    c1 = len(re.findall('[aeiou]', s)) >= 3
    c2 = re.search(r"(.)\1", s)
    c3 = [i for i in ['ab', 'cd', 'pq', 'xy'] if i in s]
    if c1 and c2 and not c3:
        P1 += 1

print(P1)
