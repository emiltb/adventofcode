data = [int(l.strip()) for l in open('data/1.in')]
print(sum(d//3-2 for d in data))

def f(n):
    ans = n//3-2
    if ans <= 0:
        return 0
    return ans + f(ans)

print(sum(f(d) for d in data))
