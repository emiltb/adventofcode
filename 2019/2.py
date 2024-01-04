from intcode import parse_intcode
from itertools import permutations
data = [int(n) for l in open('data/2.in') for n in l.strip().split(',')]

print(parse_intcode(data, 12, 2))

for i1, i2 in permutations(range(100), 2):
    if parse_intcode(data, i1, i2) == 19690720:
        print(i1*100 + i2)
        break
