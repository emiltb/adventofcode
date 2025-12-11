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



S = 'svr'
q = deque([(S, 0, [S])])

P2 = []
while q:
    node, steps, path = q.popleft()

    for next_node in graph[node]:
        if next_node == 'out':
            print(path)
            P2.append(path)
            continue
        q.append((next_node, steps + 1, path + [next_node]))

print(len([p for p in P2 if 'fft' in p and 'dac' in p]))