from collections import deque
data = [l.strip() for l in open('data/10.in')]

start = [(r,c) for r, l in enumerate(data) for c, s in enumerate(l) if s == '0']
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
rows, cols = len(data) - 1, len(data[0]) - 1

def num_trailheads(s):
    res = 0
    q = deque([s])
    visited = set([s])

    while q:
        r, c = q.popleft()

        for d in dirs:
            next_r, next_c = r + d[0], c + d[1]
            
            if next_r < 0 or next_r > rows or next_c < 0 or next_c > cols or (next_r, next_c) in visited or int(data[next_r][next_c]) - int(data[r][c]) != 1:
                continue

            res += data[next_r][next_c] == "9"
            q.append((next_r, next_c))
            visited.add((next_r, next_c))
    return res

def num_distinct_trailheads(s):
        res = 0
        q = deque([(*s, [s])])

        while q:
            r, c, trace = q.popleft()

            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                
                if next_r < 0 or next_r > rows or next_c < 0 or next_c > cols or (next_r, next_c) in trace or int(data[next_r][next_c]) - int(data[r][c]) != 1:
                    continue

                res += data[next_r][next_c] == "9"
                q.append((next_r, next_c, trace + [(next_r, next_c)]))
        return res

print(sum(num_trailheads(s) for s in start))
print(sum(num_distinct_trailheads(s) for s in start))