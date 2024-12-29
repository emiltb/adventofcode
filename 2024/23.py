from collections import defaultdict
import networkx as nx

data = [l.strip().split("-") for l in open("data/23.in")]

connections = defaultdict(set)
graph = nx.Graph()
for n1, n2 in data:
    connections[n1].add(n2)
    connections[n2].add(n1)
    graph.add_edge(n1, n2)

nodes_with_t = {k for k in connections.keys() if str(k).startswith("t")}

P1 = set()
for n1 in connections.keys():
    for n2 in connections[n1]:
        for n3 in connections[n2]:
            S = frozenset([n1, n2, n3])
            if n1 in connections[n3] and n1 != n3 and S & nodes_with_t:
                P1.add(S)

print(len(P1))

print(",".join(sorted(max(nx.find_cliques(graph), key=len))))
