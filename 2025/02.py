import re
data = [l.strip().split(',') for l in open('data/2.in')][0]
id_list = [[int(n) for n in s.split('-')] for s in data]

P1 = sum(n for n1, n2 in id_list for n in range(n1, n2 + 1) if re.match(r'^(\d+)\1$', str(n)))
P2 = sum(n for n1, n2 in id_list for n in range(n1, n2 + 1) if re.match(r'^(\d+)\1+$', str(n)))

print(P1, P2)