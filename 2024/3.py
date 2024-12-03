import re

mul_pat = re.compile(r'mul\((\d+),(\d+)\)')

data = "".join([l for l in open('data/3.in')])
ops = mul_pat.findall(data)
p1 = 0
for n1, n2 in ops:
    p1 += int(n1) * int(n2)
print(p1)


do_s = [int(s.start()) for s in re.finditer(r'do\(\)', data)]
dont_s = [int(s.start()) for s in re.finditer(r'don\'t\(\)', data)]
mul_s = {int(s.start()): [int(n) for n in s.groups()] for s in mul_pat.finditer(data)}

p2 = 0
mul_on = 1
for i in range(len(data)):
    if i in do_s: mul_on = 1
    if i in dont_s: mul_on = 0
    if i in mul_s.keys():
        p2 += mul_s[i][0] * mul_s[i][1] * mul_on
print(p2)