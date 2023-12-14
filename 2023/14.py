data = [list(l.strip()) for l in open('data/14.in')]
data

while True:
    n_moved = 0
    for r, d in enumerate(data):
        if r == 0:
            continue
        for c, s in enumerate(d):
            if s == 'O' and data[r-1][c] == '.':
                data[r][c] = '.'
                data[r-1][c] = 'O'
                n_moved += 1
    if n_moved == 0:
        break

P1 = 0
for r, d in enumerate(data):
    n_o = sum(s == 'O' for s in d)
    P1 += (len(data) - r) * n_o
print(P1)