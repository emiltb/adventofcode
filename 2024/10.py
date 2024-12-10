from collections import deque
data = [l.strip() for l in open('data/10.in')]

start = {(r,c): 0 for r, l in enumerate(data) for c, s in enumerate(l) if s == '0'}
end = [(r,c) for r, l in enumerate(data) for c, s in enumerate(l) if s == '9']
# print(data)
# print(start)
# print(end)

q = deque(end)

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while q:

    node = q.popleft()
    lq = deque([node])
    visited = set(node)
    
    while lq:
        ln = lq.popleft()
        for d in dirs:
            next_r, next_c = ln[0] + d[0], ln[1] + ln[1]
            if next_r < 0 or next_r > len(data) - 1 or next_c < 0 or next_c > len(data[0]) - 1:
                break
            if int(data[next_r][next_c]) + 1 != int(data[ln[0]][ln[1]]):
                break
            if (next_r, next_c) not in visited:
                visited.add((next_r, next_c))
                if data[next_r][next_c] == "0":
                    start[(next_r,next_c)] += 1

print(start)



