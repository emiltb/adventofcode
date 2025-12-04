data = [l.strip() for l in open('data/4.in')]

grid = {(r, c) for r in range(len(data)) for c in range(len(data[0])) if data[r][c] == '@'}

dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

P1 = 0
for r, c in grid:
    count_adjacent = 0
    for dr, dc in dirs:
        if (r + dr, c + dc) in grid:
            count_adjacent += 1
    if count_adjacent < 4:
        P1 += 1

print(P1)


removed = set()

while True:
    for r, c in grid:
        count_adjacent = 0
        for dr, dc in dirs:
            if (r + dr, c + dc) in grid:
                count_adjacent += 1
        if count_adjacent < 4:
            removed.add((r,c))
    
    if not grid & removed:
        break
    
    grid = grid - removed


print(len(removed))