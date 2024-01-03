data = [int(l.strip()) for l in open('data/1.in')]
print(sum(d//3-2 for d in data))

f = lambda n: 0 if (ans := n//3-2) <= 0 else ans + f(ans)
print(sum(f(d) for d in data))
