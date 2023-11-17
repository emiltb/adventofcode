import numpy as np
with open('inputs/input01.txt', 'r') as f:
    input01 = f.readlines()

# Part 1

# Parse all values into a list, making sure that we can recognize each elfs groups
input01 = [n.strip() for n in input01]
input01 = np.array([int(n) if n != '' else 0 for n in input01])

# Split the values into groups depending on where the array is 0 (which corresponds to blank lines in the input data)
list_divisions = np.where(input01 == 0)[0]
elf_groups = np.split(input01, list_divisions)

# Amount of calories carried by the elf with most calories
per_elf_total = [sum(L) for L in elf_groups]
print("Amount carried by elf with most calories:", max(per_elf_total))


# Part 2

# Sort the per_elf_total array to make it easy to find the top 3
per_elf_total.sort()
print("Amount carried by to three elves:", sum(per_elf_total[-3:]))
