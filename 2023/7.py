from collections import Counter
from functools import cmp_to_key
from itertools import count

data = {k: int(b) for k, b in [l.split() for l in open('2023/data/7.in')]}
symbols = "AKQJT98765432"[::-1]
c = count(1)

def compare(a,b):
    la, lb = [sorted(Counter(l).values(), reverse = True) for l in [a,b]]
    if la == lb:
        ia, ib = [[symbols.index(c) for c in x] for x in [a,b]]
        if ia > ib:
            return 1
        else:
            return -1
    if la > lb:
        return 1
    if la < lb:
        return -1
    
sorted_cards = sorted(list(data.keys()), key = cmp_to_key(compare))

P1 = sum(data[card] * rank for card, rank in zip(sorted_cards, c))
print(P1)

