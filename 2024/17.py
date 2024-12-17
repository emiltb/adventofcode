import re
data = [[int(n) for n in re.findall(r'\d+', l.strip())] for l in open('data/17.in')]

registers = {'A': data[0][0], 'B': data[1][0], 'C': data[2][0]}
program = data[4]

def get_c_op(c_op):
    if c_op <= 3:
        return c_op
    elif c_op == 4:
        return registers['A']
    elif c_op == 5:
        return registers['B']
    elif c_op == 6:
        return registers['C']
    

def adv(c_op):
    c_op = get_c_op(c_op)
    registers['A'] = int(registers['A'] / (2 ** c_op))

def bxl(c_op):
    registers['B'] = registers['B'] ^ c_op

def bst(c_op):
    c_op = get_c_op(c_op)
    registers['B'] = c_op % 8

def jnz(c_op):
    if registers['A'] == 0:
        return None
    return c_op

def bxc(c_op):
    registers['B'] = registers['B'] ^ registers['C']

def out(c_op):
    c_op = get_c_op(c_op)
    P1.append(c_op % 8)

def bdv(c_op):
    c_op = get_c_op(c_op)
    registers['B'] = int(registers['A'] / (2 ** c_op))

def cdv(c_op):
    c_op = get_c_op(c_op)
    registers['C'] = int(registers['A'] / (2 ** c_op))

instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

P1 = []
p = 0
while p < len(program) - 1:
    rc = instructions[program[p]](program[p+1])
    p = p + 2 if rc is None else rc

print(",".join(str(n) for n in P1))

P2 = []
def out(c_op):
    c_op = get_c_op(c_op)
    P2.append(c_op % 8)

instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

i = 117440
while True:
    registers = {'A': i, 'B': data[1][0], 'C': data[2][0]}
    if i % 100000 == 0:
        print(i)
    program = data[4]
    print(program)
    p = 0
    while p < len(program) - 1:
        print(f"Pointer {p}: {instructions[program[p]].__name__}({program[p+1]}) - {registers}")
        rc = instructions[program[p]](program[p+1])
        p = p + 2 if rc is None else rc

    if P2 == program:
        print(i)
        break
    i += 1
    P2 = []


