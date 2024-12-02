data = [[int(s) for s in l.strip().split()] for l in open('data/2.in')]

def is_safe(l):
    safe = 1
    for a,b in zip(l[0:], l[1:]):
        if not -3 <= a - b <= 3:
            safe = 0
        if ((a - b) > 0) != (l[0] - l[1] > 0):
            safe = 0
        if a == b:
            safe = 0
    return safe == 1

p1 = 0
for l in data:
    p1 += is_safe(l)
print(p1)

p2 = 0
for l in data:
    if is_safe(l):
        p2 += 1
    else:
        for i in range(len(l)):
            nl = list(l)
            nl.pop(i)
            if is_safe(nl):
                p2 += 1
                break
print(p2)
