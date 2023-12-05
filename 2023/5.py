data = [l.strip() for l in open("data/5.test.in")]

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
    for k in list(maps.keys())[::-1]:
        l = convert_rev(k, l)
    for s, r in seed_pairs:
        if s <= l <= (s + r):
            print(init_l)
            search = False
    l = init_l + 1

# Part 2 - revised


def contains(a, b):
    # Returns true if b is contained in a
    return (a[0] <= b[0]) and (a[1] >= b[1])


def convert_range(map_type, rng):
    if isinstance(rng[0], list):
        l = []
        for e in rng:
            l.append(convert_range(map_type, e))
        return l

    r_start, r_len = rng
    r_end = r_start + r_len
    for d_start, s_start, m_len in maps[map_type]:
        d_end = d_start + m_len
        s_end = s_start + m_len
        # print(f"comparing {s_start}-{s_end} -> {d_start}-{d_end}")
        # print(f"with {r_start}-{r_end} ->")

        if contains([s_start, s_end], [r_start, r_end]):
            # print("seed range is contained")
            return [
                r_start - s_start + d_start,
                r_end - s_end + d_end - (r_start - s_start + d_start),
            ]
        if r_start < s_start < r_end and r_end < s_end:
            # print("seed range overlaps on the left")
            r1 = [r_start, (s_start - 1) - r_start]
            c1 = convert_range(map_type, r1)
            r2 = [s_start, r_end - s_start]
            c2 = convert_range(map_type, r2)
            return [c1, c2]
        if s_start < r_start and r_start < s_end < r_end:
            # print("seed range overlaps on the right")
            r1 = [r_start, r_start - s_start]
            c1 = convert_range(map_type, r1)
            r2 = [s_end, r_end - s_end]
            c2 = convert_range(map_type, r2)
            return [c1, c2]
        if r_start < s_start and s_end < r_end:
            # print("seed range exceeds in both ends")
            r1 = [r_start, (s_start - 1) - r_start]
            r2 = [s_start, s_end - s_start]
            r3 = [s_end + 1, r_end - (s_end + 1)]
            c1 = convert_range(map_type, r1)
            c2 = convert_range(map_type, r2)
            c3 = convert_range(map_type, r3)
            return [c1, c2, c3]

    # print("everything else should fall through unaltered")
    # for d_start, s_start, r_len in maps[map_type]:
    #     if s_start <= key <= (s_start + r_len):
    #         return d_start - s_start + key
    return rng


res = convert_range("seed-to-soil", (10, 100))
res

min_loc = 1e12
for s in seed_pairs:
    print(s)
    sc = s
    for k in maps.keys():
        sc = convert_range(k, sc)
        if len(sc) > 2:
            sc = list(zip(*(iter(sc),) * 2))
        print(sc)


#     for k in maps.keys():
#         s = convert(k, s)
#     min_loc = min(s, min_loc)
# print(min_loc)
