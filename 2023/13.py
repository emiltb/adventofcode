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
    replace_list = set()
    all_n = []
    for i, l1 in enumerate(l):
        for l2 in l:
            combs = [i for i in range(len(l1)) if l1[i] != l2[i]]
            if len(combs) == 1:
                replace_list.add((i, l2))
    for item, li in replace_list:
        new_data = l.copy()
        new_data[item] = li
        for n in range(1, len(new_data)):
            if all(l1 == l2 for l1, l2 in zip(new_data[:n][::-1], new_data[n:])):
                all_n.append(n)
    p1res = f(l)
    res = [0]
    if len(all_n) == 1:
        res = all_n
    else:
        res = [n for n in all_n if n != p1res]
    return res[0] if res else 0


P2 = 0
for l in data:
    l_t = ["".join(i) for i in zip(*l)]
    P2 += 100 * g(l) + g(l_t)
print(P2)

t = """.#..#.#..
.......##
######.#.
#.##.###.
#....#.##
#....###.
######.#.
.####....
.####.#..
######.#.
#....###."""
t.split()
f(t.split())
g(t.split())

t_t = ["".join(i) for i in zip(*t.split())]
t_t
f(t_t)
g(t_t)
