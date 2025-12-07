from collections import defaultdict
data = [l.strip() for l in open('data/7.in')]

S = [(i, j) for i, r in enumerate(data) for j, c in enumerate(r) if data[i][j] == 'S'][0]
splitters = {(i,  j) for i, r in enumerate(data) for j, c in enumerate(r) if data[i][j] == '^'}

r_max = len(data)

def p1(pos, splits = set()):
    if any(p[0] == r_max for p in pos):
        return len(splits)

    new_pos = set()
    for r, c in pos:
        if (r+1, c) in splitters:
            new_pos.add((r+1, c-1))
            new_pos.add((r+1, c+1))
            splits.add((r+1, c))
        else:
            new_pos.add((r+1, c))
    
    return p1(new_pos, splits)


print(p1(set((S,))))

def p2(pos, cache):
    if pos in cache:
        return cache[pos]
    
    if pos[0] == r_max:
        return 1

    ans = 0
    r, c = pos
    if (r+1, c) in splitters:
        ans += p2((r+1, c-1), cache)
        ans += p2((r+1, c+1), cache)
    else:
        ans += p2((r+1, c), cache)

    cache[pos] = ans
    
    return ans

print(p2(S, {}))


# Other, more direct approach to part 2
pos = defaultdict(lambda: 0)
for r in data:
    if 'S' in r:
        pos[r.index('S')] = 1
        continue
    
    for i, c in enumerate(r):
        if c == '^':
            pos[i-1] += pos[i]
            pos[i+1] += pos[i]
            pos[i] = 0
print(sum(pos.values()))