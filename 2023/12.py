from ast import literal_eval
import re
from itertools import permutations

data = [
    [a, literal_eval(b)] for a, b in [l.strip().split(" ") for l in open("data/12.in")]
]


def get_arrangement(l):
    damaged = re.findall("#+", l)
    return tuple(d.count("#") for d in damaged)


def f(l):
    springs, damaged = l
    n_missing = springs.count("?")
    n_damaged = sum(damaged)
    n_working = n_missing - n_damaged

    ways = set(permutations(["."] * n_working + ["#"] * n_damaged, 7))
    c = 0
    for w in ways:
        if get_arrangement("".join(w)) == damaged:
            c += 1

    return c


P1 = 0
for l in data:
    P1 += f(l)
print(P1)
