data = [l.split() for l in open("data/13.in").read().split("\n\n")]


def f(l):
    for n in range(1, len(l)):
        if all(l1 == l2 for l1, l2 in zip(l[:n][::-1], l[n:])):
            return n
    return 0


P1 = 0
for l in data:
    l_t = ["".join(i) for i in zip(*l)]
    P1 += 100 * f(l) + f(l_t)
print(P1)
