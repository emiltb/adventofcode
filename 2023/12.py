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
    n_springs = len(springs)
    n_damaged = sum(damaged)
    n_missing = springs.count("?")
    n_known_working = springs.count(".")
    n_known_damaged = springs.count("#")
    n_working = n_springs - n_damaged

    ways = set(permutations(["."] * (n_working - n_known_working) + ["#"] * (n_damaged - n_known_damaged), n_missing))
    c = 0
    for w in ways:
        new_s = springs
        for s in w:
            new_s = new_s.replace('?', s, 1)
        if get_arrangement(new_s) == damaged:
            c += 1

    return c


P1 = 0
for i, l in enumerate(data):
    print(i)
    P1 += f(l)
print(P1)
