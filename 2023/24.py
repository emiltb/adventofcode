import re
from itertools import combinations
from sympy import Symbol, symbols, solve_poly_system

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
# p + v*t = p[i] + v[i]*t   =>   p + v*t - p[i] - v[i]*t = 0
# We need to find 6 variables (x, y, z, vx, vy, vz) and 
# the collission time for each hailstone.
# This means that the system can be solved using 9 equations, describing
# the collisions with 3 hailstones.

x, y, z, vx, vy, vz = variables = symbols('x,y,z,vx,vy,vz')
equations = []
for i, (hx, hy, hz, hvx, hvy, hvz) in enumerate(data[:3]):
    t = Symbol(f"t{i}")

    equations.append(x + vx*t - hx - hvx*t)
    equations.append(y + vy*t - hy - hvy*t)
    equations.append(z + vz*t - hz - hvz*t)
    variables += (t,)

P2 = solve_poly_system(equations, *variables)[0]
print(sum(P2[:3]))