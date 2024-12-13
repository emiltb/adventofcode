from more_itertools import split_at
import re
from math import floor


def count_tokens(scale = 0):
      res = 0
      data = split_at((l.strip() for l in open('data/13.in')), lambda x: x == '')
      for l in data:
            VAx, VAy, VBx, VBy, X, Y = [int(n) for n in re.findall(r'\d+', ''.join(l))]
            X, Y = X + scale, Y + scale
            det = VAx*VBy - VBx*VAy
            A, B = (X*VBy - VBx*Y) / det, (Y*VAx - VAy*X) / det
            if A == floor(A) and B == floor(B):
                  res += 3*int(A) + int(B)
      return res

print(count_tokens())
print(count_tokens(10000000000000))