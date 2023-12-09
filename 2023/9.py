import re
data = [[int(n) for n in re.findall('-?\d+', l.strip())] for l in open('data/9.in')]

def f(l):
    ll = [l]
    while not all(n==0 for n in l):
        l = [s2-s1 for s1, s2 in zip(l, l[1:])]
        ll.append(l)
    s = 0
    s2 = 0 
    for l in ll[::-1]:
        s += l[-1]
        s2 = l[0] - s2
    return s,s2

P1 = []
P2 = []
for l in data:
    r1, r2 = f(l)
    P1.append(r1)
    P2.append(r2)
print(sum(P1))
print(sum(P2))
