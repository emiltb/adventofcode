#%%
from itertools import compress
data = [l.strip() for l in open('data/3.in')]

gamma = ''
epsilon = ''

for i in range(len(data[0])):
    counts = {'0': 0, '1': 0}
    for d in data:
        counts[d[i]] += 1
    gamma += '0' if counts['0'] > counts['1'] else '1'
    epsilon += '1' if counts['0'] > counts['1'] else '0'

print(int(gamma, base=2) * int(epsilon, base=2))

# %%

ox_rat_mask = [True for _ in range(len(data))]
CO2_scrub_mask = [True for _ in range(len(data))]

for i in range(len(data[0])):
    counts = {'0': 0, '1': 0}
    for d in list(compress(data, ox_rat_mask)):
        counts[d[i]] += 1

    most_common = '1' if counts['1'] >= counts['0'] else '0'
    for d in list(compress(data, ox_rat_mask)):
        if d[i] != most_common:
            ox_rat_mask[data.index(d)] = False

    if len(list(compress(data, ox_rat_mask))) == 1:
        break


for i in range(len(data[0])):
    counts = {'0': 0, '1': 0}
    for d in list(compress(data, CO2_scrub_mask)):
        counts[d[i]] += 1

    least_common = '0' if counts['1'] >= counts['0'] else '1'
    for d in list(compress(data, CO2_scrub_mask)):
        if d[i] != least_common:
            CO2_scrub_mask[data.index(d)] = False

    if len(list(compress(data, CO2_scrub_mask))) == 1:
        break
    
ox_rat = int(list(compress(data, ox_rat_mask))[0], base=2)
CO2_rat = int(list(compress(data, CO2_scrub_mask))[0], base=2)
print(ox_rat * CO2_rat)

# %%
