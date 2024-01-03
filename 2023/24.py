import re
from itertools import combinations
from sympy import Symbol, solve_poly_system

data = [[int(n) for n in re.findall("-?\d+", l.strip())] for l in open("data/24.in")]

# Part 1
minval = 200000000000000
maxval = 400000000000000

P1 = 0
for (x1, y1, z1, vx1, vy1, vz1), (x2, y2, z2, vx2, vy2, vz2) in combinations(data, 2):
    try:
        t1 = (x2 - x1 + vx2 * y1 / vy2 - vx2 * y2 / vy2) / (vx1 - vy1 * vx2 / vy2)
        t2 = (y1 - y2 + vy1 * t1) / vy2
        x = x1 + vx1 * t1
        y = y1 + vy1 * t1
        if (t1 > 0 and t2 > 0 and x >= minval and x <= maxval and y >= minval and y <= maxval):  # fmt: skip
            P1 += 1
    except ZeroDivisionError:
        pass
print(P1)

# Part 2
x, y, z = Symbol('x'), Symbol('y'), Symbol('z')
vx, vy, vz = Symbol('vx'), Symbol('vy'), Symbol('vz')

equations = []
time_symbols = []

for i, (hx, hy, hz, hvx, hvy, hvz) in enumerate(data[:3]):
    t = Symbol(f"t{i}")

    equations.append(x + vx*t - hx - hvx*t)
    equations.append(y + vy*t - hy - hvy*t)
    equations.append(z + vz*t - hz - hvz*t)
    time_symbols.append(t)

P2 = solve_poly_system(equations, x, y, z, vx, vy, vz, *time_symbols)[0]
print(sum(P2[:3]))