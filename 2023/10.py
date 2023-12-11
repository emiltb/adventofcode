data = [l.strip() for l in open("data/10.in")]

# Part 1
S = [(i, l.index("S")) for i, l in enumerate(data) if "S" in l][0]


def next_move(char, indir):
    match char:
        case "|":
            if indir == (1, 0) or indir == (-1, 0):
                return indir
        case "-":
            if indir == (0, 1) or indir == (0, -1):
                return indir
        case "L":
            if indir == (1, 0):
                return (0, 1)
            if indir == (0, -1):
                return (-1, 0)
        case "J":
            if indir == (1, 0):
                return (0, -1)
            if indir == (0, 1):
                return (-1, 0)
        case "7":
            if indir == (0, 1):
                return (1, 0)
            if indir == (-1, 0):
                return (0, -1)
        case "F":
            if indir == (-1, 0):
                return (0, 1)
            if indir == (0, -1):
                return (1, 0)


found_s = False
for nm in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    P1 = 0
    pos = S
    path = [S]
    while True:
        pos = (pos[0] + nm[0], pos[1] + nm[1])
        path.append(pos)
        P1 += 1
        nm = next_move(data[pos[0]][pos[1]], indir=nm)
        if pos == S:
            print(P1 // 2)
            found_s = True
            break
        if not nm:
            break
    if found_s:
        break

# Part 2
nodes_inside = 0

for r, l in enumerate(data):
    inside = False
    previous_corner = None

    for c, s in enumerate(l):
        if previous_corner == "L" and s == "7" and (r, c) in path:
            inside = not inside

        if previous_corner == "F" and s == "J" and (r, c) in path:
            inside = not inside

        if (r, c) in path and s in "|7FJL":
            inside = not inside

        if s in "7FJL":
            previous_corner = s

        if inside == True and (r, c) not in path:
            nodes_inside += 1

print(nodes_inside)
