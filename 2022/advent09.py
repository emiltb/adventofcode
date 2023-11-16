from math import sqrt

with open("inputs/input09.txt", "r") as f:
    data = f.readlines()

H_moves = [(m[0], int(m[1])) for m in [s.strip().split() for s in data]]

# Part 1
H_pos = [0, 0]
T_pos = [0, 0]

H_log = []
T_log = []

for m in H_moves:
    d = m[0]
    n = m[1]
    for s in range(n):
        if d == "U":
            H_pos[1] += 1
        if d == "D":
            H_pos[1] -= 1
        if d == "L":
            H_pos[0] -= 1
        if d == "R":
            H_pos[0] += 1

        x_dist = H_pos[0] - T_pos[0]
        y_dist = H_pos[1] - T_pos[1]
        if sqrt(x_dist**2 + y_dist**2) > sqrt(2):
            x_dist = x_dist / abs(x_dist) if x_dist != 0 else x_dist
            y_dist = y_dist / abs(y_dist) if y_dist != 0 else y_dist
            T_pos[0] += x_dist
            T_pos[1] += y_dist
        T_log.append(T_pos.copy())

T_log_set = {(x, y) for (x, y) in T_log}
print("Number of unique positions held by tail:", len(T_log_set))


# Part 2
# Solution is basically identical, except each part of the rope has to track
# the previous section
R_pos = [[0, 0] for n in range(10)]
T_log = []


for m in H_moves:
    d = m[0]
    n = m[1]
    for s in range(n):
        if d == "U":
            R_pos[0][1] += 1
        if d == "D":
            R_pos[0][1] -= 1
        if d == "L":
            R_pos[0][0] -= 1
        if d == "R":
            R_pos[0][0] += 1

        for s in range(1, 10):
            x_dist = R_pos[s - 1][0] - R_pos[s][0]
            y_dist = R_pos[s - 1][1] - R_pos[s][1]
            if sqrt(x_dist**2 + y_dist**2) > sqrt(2):
                x_dist = x_dist / abs(x_dist) if x_dist != 0 else x_dist
                y_dist = y_dist / abs(y_dist) if y_dist != 0 else y_dist
                R_pos[s][0] += x_dist
                R_pos[s][1] += y_dist
        T_log.append(R_pos[9].copy())

T_log_set = {(x, y) for (x, y) in T_log}
print("Number of unique positions held by tail:", len(T_log_set))
