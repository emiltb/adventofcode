from z3 import Ints, Solver, sat
from more_itertools import split_at
import re

A, B = Ints('A B')

def count_tokens(scale = 0):
      res = 0
      data = split_at((l.strip() for l in open('data/13.in')), lambda x: x == '')
      for l in data:
            s = Solver()
            VAx, VAy, VBx, VBy, X, Y = [int(n) for n in re.findall(r'\d+', ''.join(l))]
            X, Y = X + scale, Y + scale
            s.add(A*VAx + B*VBx == X, A*VAy + B*VBy == Y)
            r = s.check()
            if r == sat:
                  m = s.model()
                  res += 3*m[A].as_long() + m[B].as_long()
      return res

print(count_tokens())
print(count_tokens(10000000000000))
