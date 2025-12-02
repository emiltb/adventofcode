import re
data = [[int(n) for n in s.split('-')] for s in [l.strip().split(',') for l in open('data/2.in')][0]]

for pattern in (r'^(\d+)\1$', r'^(\d+)\1+$'):
    print(sum(n for n1, n2 in data for n in range(n1, n2 + 1) if re.match(pattern, str(n))))
