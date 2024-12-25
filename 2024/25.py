from more_itertools import split_at
from itertools import product

data = [l.strip() for l in open('data/25.in')]
items = [l for l in split_at(data, lambda x: x == '')]

locks = [l[1:] for l in items if l[0]=='#####']
keys = [l[:-1] for l in items if l[-1]=='#####']

def get_digits(s):
    digs = []
    for n in s:
        dig = [0] * len(n[0])
        for d in n:
            for i, c in enumerate(d):
                dig[i] += c == '#'
        digs.append(dig)
    return digs

lock_digits = get_digits(locks)
key_digits = get_digits(keys)
print(sum(all(((d1 + d2) <= 5 for d1, d2 in zip(l, k))) for l, k in product(lock_digits, key_digits)))
