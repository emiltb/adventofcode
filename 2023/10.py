data = [l.strip() for l in open("data/10.in")]

S = [(i, l.index("S")) for i, l in enumerate(data) if "S" in l][0]


def next_move(char, indir):
    match char:
        case "|":
            return indir
        case "-":
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


P1 = 1

first_move = (0, 1)
next_pos = (S[0], S[1] + 1)
nm = next_move(data[next_pos[0]][next_pos[1]], indir=(0, 1))
while next_pos != S:
    P1 += 1
    next_pos = (next_pos[0] + nm[0], next_pos[1] + nm[1])
    nm = next_move(data[next_pos[0]][next_pos[1]], indir=nm)
print(P1 // 2)
