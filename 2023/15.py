from collections import defaultdict
data = "".join([l.strip() for l in open('data/15.in')]).split(',')

# Part 1
def f(e):
    n = 0
    for s in e:
        n = ((n + ord(s)) * 17) % 256
    return n

P1 = 0
for e in data:
    P1 += f(e)
print(P1)

# Part 2
boxes = defaultdict(dict)
for e in data:
    if "=" in e:
        box, op = e.split("=")
        lens = {box: int(op)}
        if box in boxes[f(box)]:
            boxes[f(box)][box] = int(op)
        else: 
            boxes[f(box)].update(lens)
    if "-" in e:
        box, _ = e.split('-')
        if box in boxes[f(box)]:
            boxes[f(box)].pop(box)

P2 = 0
for box, lenses in boxes.items():
    for n, lens in enumerate(lenses.values(), 1):
        P2 += (box + 1) * n * lens
print(P2)
