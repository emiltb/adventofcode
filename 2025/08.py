from itertools import combinations
from functools import reduce
from collections import defaultdict

data = [tuple(int(n) for n in l.strip().split(',')) for l in open('data/8.in')]

# Part 1
n_cons = 1000

def dist(a, b):
    return int(((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2) ** (1/2))

dists = [(dist(*l), *l) for l in combinations(data, 2)]

dists.sort()

circuits = [{a,b} for _, a, b in dists[:n_cons]]

def combine_elements(circuits):
    circuit_list = []
    while circuits:
        next_element = circuits.pop()
        if not any(next_element & cc for cc in circuit_list):
            circuit_list.append(next_element)
        else:
            for idx, cc in enumerate(circuit_list):
                overlap = next_element & cc
                if overlap:
                    circuit_list[idx] |= next_element

    return circuit_list

prev_length = 0
for _ in range(10):
    circuits = combine_elements(circuits)

    lengths = sorted([len(c) for c in circuits], reverse=True)
    if lengths == prev_length:
        print(reduce(int.__mul__, lengths[:3]))
        break
    prev_length = lengths

# Part 2
circuits = [{a,b} for d, a, b in dists]
graph = defaultdict(set)

for a, b in circuits:
    graph[a].add(b)
    graph[b].add(a)

    if graph.keys() == set(data):
        print(a[0]*b[0])
        break
