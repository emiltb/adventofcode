from functools import reduce

raw_data = [l for l in open('data/6.in')]
data = [l.strip().split() for l in raw_data]

operators = [int.__mul__ if o == '*' else int.__add__ for o in data[-1]]

numbers = [[] for _ in range(len(data[0]))]

for r in data[:-1]:
    for i, n in enumerate(r):
        numbers[i].append(int(n))

P1 = sum(reduce(o, n) for o, n in zip(operators, numbers))
print(P1)

data = [l.replace('\n', '') for l in raw_data][:-1]

data_transposed = ['' for _ in range(len(data[0]))]
for r in data:
    for n in range(len(data[0])):
        data_transposed[n] += r[n]

numbers = [[]]
for d in data_transposed:
    if (v := d.strip()) != '':
        numbers[-1].append(int(v))
    else:
        numbers.append([])
P2 = sum(reduce(o, n) for o, n in zip(operators, numbers))
print(P2)
