import re

data = "".join([l for l in open('data/3.in')])

ops = re.findall(r'mul\((\d+),(\d+)\)', data)
p1 = 0
for n1, n2 in ops:
    p1 += int(n1) * int(n2)
print(p1)

p2 = 0
mul_on = 1
for m in re.finditer(r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))', data):
    n1, n2, do, dont = m.groups()
    if do: mul_on = 1
    if dont: mul_on = 0
    if n1 and n2:
        p2 += int(n1) * int(n2) * mul_on
print(p2)