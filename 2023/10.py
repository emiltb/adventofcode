data = [l.strip() for l in open("data/10.in")]

visited = [(i, l.index("S")) for i, l in enumerate(data) if "S" in l]
S = visited[0]


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
    while True:
        pos = (pos[0] + nm[0], pos[1] + nm[1])
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
