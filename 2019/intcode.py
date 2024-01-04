def add(mem, x, y, p):
    mem[p] = mem[x] + mem[y]

def multiply(mem, x, y, p):
    mem[p] = mem[x] * mem[y]
    
ops = {
        1: add,
        2: multiply
    }

def parse_intcode(mem, in1, in2):
    mem = list(mem)
    mem[1] = in1
    mem[2] = in2

    p = 0
    while mem[p] != 99:
        ops[mem[p]](mem, mem[p+1], mem[p+2], mem[p+3])
        p += 4
    return mem[0]
