
from collections import deque
wire_input, gate_input = [[s.strip() for s in l.split('\n') if s != ''] for l in open('data/24.in').read().split('\n\n')]

wires = {v.split(':')[0]: int(v.split(':')[1].strip()) for v in wire_input}

gates = []
for g in gate_input:
    wire1, op, wire2, _, wire3 = g.split()
    for w in [wire1, wire2, wire3]:
        if w not in wires:
            wires[w] = None
    gates.append((wire1, wire2, op, wire3))
initial_wires = wires.copy()

ops = {
    'AND': int.__and__,
    'OR': int.__or__,
    'XOR': int.__xor__,
}

q = deque(gates)

while q:
    w1, w2, op, w3 = q.popleft()

    if wires[w1] is not None and wires[w2] is not None:
        wires[w3] = ops[op](wires[w1],wires[w2])
    else:
        q.append([w1, w2, op, w3])

print(int(''.join([str(v) for k, v in sorted(wires.items(), reverse=True) if k.startswith('z')]), base = 2))
