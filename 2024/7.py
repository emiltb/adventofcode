import re
from itertools import product
data = [[int(n) for n in re.findall(r"\d+", l.strip())] for l in open('data/7.in')]

ops = {
    '+': int.__add__,
    '*': int.__mul__,
    '|': lambda n1, n2: int(str(n1)+str(n2))
}

def check_nums(o):
    res = 0
    for l in data:
        for ways in product(o, repeat=len(l) - 2):
            n = l[1]
            for op, d in zip(ways, l[2:]):
                n = ops[op](n, d)
                if n > l[0]:
                    break
            if n == l[0]:
                res += l[0]
                break
    print(res)

check_nums('+*')
check_nums('+*|')