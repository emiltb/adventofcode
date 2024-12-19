towels, designs = open('data/19.in').read().split('\n\n')
towels = tuple(t.strip() for t in towels.split(','))
designs = [d.strip() for d in designs.split()]

def f(string, idx, cache):
    if (string, idx) in cache: 
        return cache[(string, idx)]
    
    ans = 0

    if len(string[idx:]) == 0: 
        return 1
    
    for r in [len(t) for t in towels if string[idx:].startswith(t)]: 
        ans += f(string, idx + r, cache)

    cache[(string, idx)] = ans
    return ans

print(sum(f(d, 0, {}) > 0 for d in designs))
print(sum(f(d, 0, {}) for d in designs))
