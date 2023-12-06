import re

time, dist = [[int(n) for n in re.findall("\d+", l)] for l in open("data/6.in")]

P1 = 1
for ti, di in zip(time, dist):
    wins = 0
    for charge in range(1, ti + 1):
        new_dist = charge * (ti - charge)
        if new_dist > di:
            wins += 1
    P1 *= wins
print(P1)

time = int("".join([str(s) for s in time]))
dist = int("".join([str(s) for s in dist]))

P2 = 0
for charge in range(1, time + 1):
    new_dist = charge * (time - charge)
    if new_dist > dist:
        P2 += 1
print(P2)
