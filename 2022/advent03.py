with open('inputs/input03.txt', 'r') as f:
    data = f.readlines()

# Part 1
# Strip newlines
rucksacks = [s.strip() for s in data]
# Split string halfway
compartments = [(set(s[:len(s)//2]),set(s[len(s)//2:])) for s in rucksacks]
# Find intersection of two sets and convert the set back to a string
double_items = [''.join(s[0] & s[1]) for s in compartments]

letters = {l:(ord(l)-96) for l in 'abcdefghijklmnopqrstuvwxyz'}
letters = letters | {(key.upper()):(value+26) for (key, value) in letters.items()}

total_priority = sum([letters[s] for s in double_items])
print('Total priority of items:', total_priority)

# Part 2
elf_groups = zip(*(iter(rucksacks),) * 3)
elf_group_sets = [[set(s) for s in l] for l in elf_groups]
common_items_per_group = [''.join(set.intersection(*s)) for s in elf_group_sets]

total_priority_for_badges = sum([letters[s] for s in common_items_per_group])
print('Total priority of badges:', total_priority_for_badges)
