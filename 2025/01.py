from collections import deque, Counter

data = [l.strip() for l in open("data/1.in")]

dial = deque(range(100))
dial.rotate(50)
P1 = Counter()

for r in data:
    d = r[0]
    l = int(r[1:])
    dial.rotate(-l if d == "R" else l)
    P1[dial[0]] += 1

print(P1[0])


dial = deque(range(100))
dial.rotate(50)
P2 = Counter()

for r in data:
    d = r[0]
    l = int(r[1:])
    for _ in range(l):
        dial.rotate(-1 if d == "R" else 1)
        P2[dial[0]] += 1

print(P2[0])
