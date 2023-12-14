data = [list(l.strip()) for l in open('data/14.in')]

# Part 1
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

# Part 2
def cycle(D):
    for dir in 'nwse':
        while True:
            n_moved = 0
            for r, d in enumerate(D):
                if r == 0:
                    continue
                for c, s in enumerate(d):
                    if s == 'O' and D[r-1][c] == '.':
                        D[r][c] = '.'
                        D[r-1][c] = 'O'
                        n_moved += 1
            if n_moved == 0:
                break
        D = [list(l) for l in zip(*D[::-1])]
    return D

data = [list(l.strip()) for l in open('data/14.in')]
org_data = data
n = 0
while True:
    n += 1
    data = cycle(data)
    load = 0
    for r, d in enumerate(data):
        n_o = sum(s == 'O' for s in d)
        load += (len(data) - r) * n_o
    print(n, load)
    if n > 200:
        break

# I looked at the output here and determined that a cycle of length 18
# starts at n = 136. We can then use the Chinese remainder theorem.
# Since (1000000000 - 136) % 18 = 0 we know that the load at n = 136 is equal 
# to the load at n = 1000000000
