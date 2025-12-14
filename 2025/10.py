from heapq import heappop, heappush
import pulp

data = [l.strip().split() for l in open('data/10.in')]

P1 = 0
for d in data:
    lights, *buttons, _ = d
    lights = int(lights[1:-1][::-1].replace('.','0').replace('#','1'), base=2)
    buttons = [{eval(l)} for l in buttons]

    q = [(0, 0b0, b) for b in buttons]

    while q:
        presses, state, button = heappop(q)

        for b in button:
            if isinstance(b, int):
                state ^= 1 << b
            else:
                for n in b:
                    state ^= 1 << n

        if state == lights:
            P1 += presses + 1
            break

        for b in buttons:
            next_node = (presses + 1, state, b)
            heappush(q, next_node)

print(P1)

P2 = 0
for d in data:
    _, *buttons, joltage = d

    buttons = [[eval(l)] for l in buttons]
    joltage = eval(joltage.replace('{','[').replace('}',']'))

    num_vars = len(buttons)
    variables = [pulp.LpVariable(f'x{i}', cat='Integer') for i in range(num_vars)]

    prob = pulp.LpProblem("Integer_System", pulp.LpMinimize)
    prob += sum(variables)
    for var in variables:
        prob += var >= 0

    lhs = []
    for row, indices in enumerate(buttons):
        if isinstance(indices[0], tuple):
            indices = [n for t in indices for n in t]

        col = []
        for n in range(len(joltage)):
            if n in indices:
                col.append(1)
            else:
                col.append(0)
        lhs.append(col)

    for l, r in zip(zip(*lhs), joltage):
        total = sum(variables[i] for i, v in enumerate(l) if v)
        prob += (total == r)

    status = prob.solve(pulp.PULP_CBC_CMD(msg=False))
    P2 += int(sum(v.varValue for v in variables))

print(P2)