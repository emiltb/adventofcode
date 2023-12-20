from itertools import groupby
import re
from collections import namedtuple

part = namedtuple("part", "x m a s")

data = [l.strip() for l in open("data/19.in")]
rules, parts = [list(group) for k, group in groupby(data, bool) if k]

parts = [part(*[int(n) for n in re.findall(r"(\d+)", s)]) for s in parts]


def get_rule(l):
    name, rule = l.split("{")
    rule_parts = rule[:-1].split(",")

    rule_elements = []
    default_dest = ""
    for r in rule_parts:
        e = r.split(":")
        match e:
            case test, dest:
                rule_elements.append([test[0], test[1], int(test[2:]), dest])
            case dest:
                default_dest = dest[0]

    def evaluate_rule(p):
        for var, op, val, dest in rule_elements:
            if op == ">":
                if getattr(p, var) > val:
                    return dest
            if op == "<":
                if getattr(p, var) < val:
                    return dest
        return default_dest

    return name, evaluate_rule


all_rules = {name: rule for name, rule in [get_rule(r) for r in rules]}

P1 = []
for p in parts:
    next_rule = all_rules["in"](p)
    while next_rule not in ("A", "R"):
        next_rule = all_rules[next_rule](p)
    if next_rule == "A":
        P1.append(p)

print(sum(sum(p) for p in P1))
