from ast import literal_eval
import re
from itertools import permutations

data = [
    [a, literal_eval(b)] for a, b in [l.strip().split(" ") for l in open("data/12.test.in")]
]


def get_arrangement(l):
    damaged = re.findall("#+", l)
    return tuple(d.count("#") for d in damaged)


def f(l):
    springs, damaged = l
    n_springs = len(springs)
    n_damaged = sum(damaged)
    n_missing = springs.count("?")
    n_working = n_springs - n_damaged

    ways = list(set(permutations(["."] * n_working + ["#"] * n_damaged, n_missing)))
    print(ways)
    c = 0
    for w in ways:
        new_s = springs
        for s in w:
            new_s = new_s.replace('?', s, 1)
        if get_arrangement(new_s) == damaged:
            c += 1

    return c


P1 = 0
for i, l in enumerate(data[0:1]):
    print(i)
    P1 += f(l)
print(P1)

