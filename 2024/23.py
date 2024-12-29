from collections import defaultdict
data = [l.strip().split('-') for l in open('data/23.test.in')]

connections = defaultdict(set)
for n1, n2 in data:
    connections[n1].add(n2)
    connections[n2].add(n1)

nodes_with_t = {k for k in connections.keys() if str(k).startswith('t')}

P1 = set()
for n1 in connections.keys():
    for n2 in connections[n1]:
        for n3 in connections[n2]:
            S = frozenset([n1, n2, n3])
            if n1 in connections[n3] and n1 != n3 and S & nodes_with_t:
                P1.add(S)

print(len(P1))

#P2 = set()
#for k, v in connections.items():
#    S = set([k, *v])
#    print(k, v, S)
#    for k1 in v:
#        # print("\t", k1, connections[k1])
#        print(set([k1, *connections[k1]]))
#        S &= set([k1, *connections[k1]])
#    print(S)

for k in connections:
    print(k, connections[k])
