from collections import Counter
from functools import cmp_to_key
from itertools import count

data = {k: int(b) for k, b in [l.split() for l in open('data/7.in')]}
symbols = "AKQJT98765432"[::-1]

def compare(a,b):
    la, lb = [sorted(Counter(l).values(), reverse = True) for l in [a,b]]
    if la == lb:
        ia, ib = [[symbols.index(c) for c in x] for x in [a,b]]
        if ia > ib:
            return 1
    if la > lb:
        return 1
    return -1
    
sorted_cards = sorted(data.keys(), key = cmp_to_key(compare))

P1 = sum(data[card] * rank for card, rank in zip(sorted_cards, count(1)))
print(P1)
