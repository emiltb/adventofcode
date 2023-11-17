import re
from copy import deepcopy

with open("inputs/input05.txt", "r") as f:
    data = f.readlines()

# Parse the data into stacks and instructions
stacks_raw = data[:8][::-1]
stacks_simplified = [l[1::4] for l in stacks_raw]
stacks = {i: [s[i] for s in stacks_simplified if s[i] != " "] for i in range(len(stacks_simplified[0]))}

instructions_raw = data[10:]
instructions = [[int(n) for n in re.findall("[\d]+", s)] for s in instructions_raw]

# Part 1
stacks_part1 = deepcopy(stacks)
def move(n, src, dst):
    for _ in range(n):
        pick_item = stacks_part1[src - 1].pop()
        stacks_part1[dst - 1].append(pick_item)

# Perform all movements
[move(*i) for i in instructions]

final_arrangement = "".join([items[-1] for (key, items) in stacks_part1.items()])
print("Final arrangement is:", final_arrangement)

# Part 2
stacks_part2 = deepcopy(stacks)
def move2(n, src, dst):
    pick_items = stacks_part2[src - 1][-n:]
    for _ in range(n):
        stacks_part2[src - 1].pop()
    stacks_part2[dst - 1] = stacks_part2[dst - 1] + pick_items

# Perform all movements
[move2(*i) for i in instructions]

final_arrangement_9001 = "".join([items[-1] for (key, items) in stacks_part2.items()])
print("Final arrangement is with CrateMover9001:", final_arrangement_9001)
