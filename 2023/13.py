from itertools import combinations

data = [l.split() for l in open("data/13.in").read().split("\n\n")]


# Part 1
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


# Part 2
def g(l):
    for n in range(1, len(l)):
        l1 = l[:n][::-1]
        l2 = l[n:]

        rowpairs = ((x,y) for x,y in zip(l1,l2))
        rowdiffs = sum(n1!=n2 for r1,r2 in rowpairs for n1,n2 in zip(r1,r2))
        if rowdiffs == 1:
            return n
    return 0

P2 = 0
for l in data:
    l_t = ["".join(i) for i in zip(*l)]
    P2 += 100 * g(l) + g(l_t)
print(P2)


