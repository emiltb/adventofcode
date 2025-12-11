from collections import deque
data = [l.strip().replace(':','').split() for l in open('data/11.in')]
graph = {k: {*v} for k, *v in data}


S = 'you'
q = deque([(S, [S])])

P1 = []
while q:
    node, path = q.popleft()

    for next_node in graph[node]:
        if next_node == 'out':
            P1.append(path)
            continue
        q.append((next_node, path + [next_node]))

print(len(P1))


def find(in_node, out_node, cache):
    if (in_node, out_node) in cache:
        return cache[(in_node, out_node)]
    if in_node == out_node:
        return 1
    
    res = sum(find(new_in_node, out_node, cache) for new_in_node in graph.get(in_node, []))
    cache[(in_node, out_node)] = res
    return res

P2 = (find('svr', 'dac', {}) * find('dac', 'fft', {}) * find('fft', 'out', {}) +
      find('svr', 'fft', {}) * find('fft', 'dac', {}) * find('dac', 'out', {}))

print(P2)