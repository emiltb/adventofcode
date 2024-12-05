from collections import defaultdict
data = [l.strip() for l in open('data/5.in')]

rules = defaultdict(list)
for a, b in [l.split('|') for l in data[:data.index('')]]:
    rules[a].append(b)
pages = [l.split(',') for l in data[data.index('')+1:]]

p1 = 0
not_sorted = []
for p in pages:
    sorted = True
    for i, n in enumerate(p):
        for m in p[i:]:
            if n in rules[m]:
                sorted = False
    if sorted:
        p1 += int(p[len(p)//2])
    else:
        not_sorted.append(p)
print(p1)

p2 = 0
for p in not_sorted:
    q = list(p)
    visited = dict()
    while q:
        v = q.pop()
        visited[v] = [n for n in rules[v] if n in p]
        
    res = [(k, len(v)) for k, v in visited.items()]
    res.sort(key=lambda tup: tup[1], reverse=True)
    p2 += int([a for a, _ in res][len(res)//2])
print(p2)
