from collections import Counter
from functools import cmp_to_key
from itertools import count, combinations_with_replacement

data = {k: int(b) for k, b in [l.split() for l in open("data/7.in")]}

# Part 1
symbols = "AKQJT98765432"[::-1]


def s_compare(s, find_max=False):
    def compare(a, b):
        max_a, max_b = a, b
        if find_max:
            max_a, max_b = [find_max_equivalent_card(x) for x in [a, b]]
        la, lb = [sorted(Counter(l).values(), reverse=True) for l in [max_a, max_b]]
        if la == lb:
            ia, ib = [[s.index(c) for c in x] for x in [a, b]]
            if ia > ib:
                return 1
        if la > lb:
            return 1
        return -1

    return compare


sorted_cards = sorted(data.keys(), key=cmp_to_key(s_compare(symbols)))
P1 = sum(data[card] * rank for card, rank in zip(sorted_cards, count(1)))
print(P1)

# Part 2
new_symbols = "AKQT98765432J"[::-1]


def find_max_equivalent_card(d):
    n_j = d.count("J")
    if n_j == 0:
        return d

    sym_rep = combinations_with_replacement(new_symbols[1:], n_j)
    new_cards = []
    for s in sym_rep:
        dr = d
        for n in s:
            dr = dr.replace("J", n, 1)
        new_cards.append(dr)
    return sorted(new_cards, key=cmp_to_key(s_compare(new_symbols)))[-1]


sorted_cards = sorted(
    data.keys(), key=cmp_to_key(s_compare(new_symbols, find_max=True))
)
P2 = sum(data[card] * rank for card, rank in zip(sorted_cards, count(1)))
print(P2)
