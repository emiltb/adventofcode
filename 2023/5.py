data = [l.strip() for l in open("data/5.in")]

# Part 1
seeds = [[int(n) for n in s.split()] for s in data[0].split(":")[1:]][0]

maps = dict()
for d in data[2:]:
    if "map" in d:
        map_type = d.split()[0]
        maps[map_type] = []
    elif d != "":
        numbers = [int(n) for n in d.split()]
        maps[map_type].append(numbers)


def convert(map_type, key):
    for d_start, s_start, r_len in maps[map_type]:
        if s_start <= key <= (s_start + r_len):
            return d_start - s_start + key
    return key


min_loc = 1e12
for s in seeds:
    for k in maps.keys():
        s = convert(k, s)
    min_loc = min(s, min_loc)
print(min_loc)

# Part 2
seed_pairs = list(zip(*(iter(seeds),) * 2))


def convert_rev(map_type, key):
    for d_start, s_start, r_len in maps[map_type]:
        if d_start <= key <= (d_start + r_len):
            return s_start - d_start + key
    return key


l = 0
search = True
while search:
    init_l = l
    next_l = l + 1
    for k in list(maps.keys())[::-1]:
        l = convert_rev(k, l)
    for s, r in seed_pairs:
        if s <= l <= (s + r):
            print(init_l)
            search = False
    l = next_l
