towels, designs = open('data/19.in').read().split('\n\n')
towels = tuple(t.strip() for t in towels.split(','))
designs = [d.strip() for d in designs.split()]

def f(string, i, cache):
    if (string, i) in cache: 
        return cache[(string, i)]
    
    if len(string[i:]) == 0: 
        return 1
    
    ans = 0
    for r in [len(t) for t in towels if string[i:].startswith(t)]: 
        ans += f(string, i + r, cache)

    cache[(string, i)] = ans
    return ans

solution = [f(d, 0, {}) for d in designs] 
print(sum(s > 0 for s in solution))
print(sum(s for s in solution))