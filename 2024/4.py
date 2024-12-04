data = [l.strip() for l in open('data/4.in')]

rs = len(data)
cs = len(data[0])

p1 = 0

# Horizontal
for l in data:
    p1 += (l+l[::-1]).count('XMAS')

# Vertical
for i in range(cs):
    s = ''.join(l[i] for l in data)
    p1 += (s+s[::-1]).count('XMAS')

# Diagonals
for r in range(rs):
    c = 0
    s = data[r][c]

    while c + 1 >= 0 and r - 1 >= 0:
        c += 1
        r -= 1
        s += data[r][c]
    p1 += (s + s[::-1]).count('XMAS')


for c in range(1, cs):
    r = rs - 1
    s = data[r][c]

    while c + 1 < cs and r - 1 >= 0:
        c += 1
        r -= 1
        s += data[r][c]

    p1 += (s + s[::-1]).count('XMAS')

for r in range(rs)[::-1]:
    c = 0
    s = data[r][c]

    while r + 1 < rs and c + 1 < cs:
        r += 1
        c += 1
        s += data[r][c]

    p1 += (s + s[::-1]).count('XMAS')

for c in range(1, cs):
    r = 0
    s = data[r][c]

    while r + 1 < rs and c + 1 < cs:
        r += 1
        c += 1
        s += data[r][c]

    p1 += (s + s[::-1]).count('XMAS')

print(p1)


def check_pos(p):
    r, c = p
    diag1 = data[r][c] + data[r+1][c+1] + data[r+2][c+2]
    diag2 = data[r+2][c] + data[r+1][c+1] + data[r][c+2]
    return (diag1 in ('MAS','SAM')) and (diag2 in ('MAS','SAM'))

print(sum(check_pos((r,c)) for r in range(rs-2) for c in range(cs-2)))
