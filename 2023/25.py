import networkx as nx

data = [l.strip() for l in open("data/25.in")]

g = nx.Graph()

for d in data:
    src, rest = d.split(":")
    rest = rest.split()

    for n in rest:
        g.add_edge(src, n)

edges_to_cut = nx.minimum_edge_cut(g)

if len(edges_to_cut) == 3:
    g.remove_edges_from(edges_to_cut)

    g1, g2 = nx.connected_components(g)

    print(len(g1) * len(g2))
