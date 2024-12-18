from collections import deque
grid = [tuple(int(n) for n in l.strip().split(',')[::-1]) for l in open('data/18.in')]
end = (70,70)

def f(i, p2 = False):
    q = deque([(0,0,0)])
    visited = set([(0,0)])

    while q:
        steps, r, c = q.popleft()

        if (r,c) == end:
            if not p2: print(steps)
            break

        for next_r, next_c in [(r,c+1), (r,c-1), (r+1,c), (r-1,c)]:
            if (next_r, next_c) in grid[:i] or (next_r, next_c) in visited:
                continue

            if not 0 <= next_r <= end[0] or not 0 <= next_c <= end[1]:
                continue

            q.append((steps + 1, next_r, next_c))
            visited.add((next_r, next_c))

    return r,c

f(1024)

for i in range(len(grid), 0, -1):
    r, c = f(i, p2 = True)

    if (r,c) == end:
        print(grid[i][::-1])
        break
