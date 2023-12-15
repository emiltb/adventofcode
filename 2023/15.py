data = "".join([l.strip() for l in open('data/15.in')])

P1 = 0
n = 0
for s in data:
    if s == ",":
        P1 += n
        n = 0
        continue
    n = ((n + ord(s)) * 17) % 256
else:
    P1 += n
print(P1)
