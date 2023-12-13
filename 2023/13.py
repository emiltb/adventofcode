from itertools import count
data = [l.split() for l in open('data/13.test.in').read().split('\n\n')]

def f(d):
    rmax = (0,0)
    for i in range(len(d)-1):
        n = 0
        while True:
            try:
                if d[i - n] == d[i + 1 + n]:
                    n += 1
                else:
                    break
            except IndexError:
                return n + 1
    return 0

P1 = 0
for l in data:
    l_t = [''.join(i) for i in zip(*l)]
    P1 += 100 * f(l) + f(l_t)
print(P1)