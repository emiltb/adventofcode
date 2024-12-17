import re
data = [[int(n) for n in re.findall(r'\d+', l.strip())] for l in open('data/17.in')]

registers = {'A': data[0][0], 'B': data[1][0], 'C': data[2][0]}
program = data[4]

def adv(c_op):
    registers['A'] = int(registers['A'] / (2 ** c_op))

def bxl():
    pass

def bst():
    pass

def jnz():
    pass

def bxc():
    pass

def out():
    pass

def bdv():
    pass

def cdv():
    pass

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

P1 = ''

print(instructions.items())
print(registers)

for p in program:
    print(p)

print(data)
adv(0)
print(registers)