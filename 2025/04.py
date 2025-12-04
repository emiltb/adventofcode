data = [l.strip() for l in open('data/4.in')]
grid = {(r, c) for r in range(len(data)) for c in range(len(data[0])) if data[r][c] == '@'}
dirs = {(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}

P1 = 0
for r, c in grid:
    if sum(1 for dr, dc in dirs if (r + dr, c + dc) in grid) < 4: 
        P1 += 1

print(P1)

P2 = set()
while True:
    for r, c in grid:
        if sum(1 for dr, dc in dirs if (r + dr, c + dc) in grid) < 4:
            P2.add((r,c))
    
    if not grid & P2:
        break
    
    grid = grid - P2

print(len(P2))
