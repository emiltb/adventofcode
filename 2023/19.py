from itertools import groupby
import re
from collections import namedtuple, deque

part = namedtuple("part", "x m a s")

data = [l.strip() for l in open("data/19.in")]
rules, parts = [list(group) for k, group in groupby(data, bool) if k]

parts = [part(*[int(n) for n in re.findall(r"(\d+)", s)]) for s in parts]


# Part 1
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


# Part 2
def get_rule_range(l):
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

    def evaluate_rule_range(p):
        for var, op, val, dest in rule_elements:
            rule_range = p[1][var]
            if op == ">":
                new_range = [val + 1, rule_range[1]]
                excluded_range = [rule_range[0], val + 1]
            if op == "<":
                new_range = [rule_range[0], val]
                excluded_range = [val, rule_range[1]]
            if new_range[1] > new_range[0]:
                new_part = (dest, p[1].copy())
                new_part[1][var] = new_range
                excluded_part = p[1].copy()
                excluded_part[var] = excluded_range
                p = (name, excluded_part)
                if dest == "A":
                    A.append(new_part[1])
                elif dest != "R":
                    q.append(new_part)
        if default_dest == "A":
            A.append(p[1])
        elif default_dest != "R":
            q.append((default_dest, p[1]))

    return name, evaluate_rule_range


all_rules = {name: rule for name, rule in [get_rule_range(r) for r in rules]}

start_part = {"x": [1, 4001], "m": [1, 4001], "a": [1, 4001], "s": [1, 4001]}

A = []
q = deque([("in", start_part)])
while q:
    rule_name, part = q.popleft()
    all_rules[rule_name]((rule_name, part))


P2 = 0
for p in A:
    p_val = 1
    for v in p.values():
        p_val *= v[1] - v[0]
    P2 += p_val
print(P2)
