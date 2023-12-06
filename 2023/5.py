from time import time

data = [l.strip() for l in open("data/5.in")]

# Part 1
start_time = time()
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
print(f"Part 1 time: {time() - start_time:.5f} s")

# Part 2
start_time = time()
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
part2_time = time() - start_time
print(f"Part 2 time: {part2_time:.5f} s")


# Part 2 - revised
start_time = time()


def convert_range(map_type, rng):
    converted_ranges = []

    for d_start, s_start, m_len in maps[map_type]:
        s_end = s_start + m_len

        new_ranges = []
        while rng:
            start, end = rng.pop()

            interval_before = (start, min(end, s_start))
            interval_contained = (max(start, s_start), min(s_end, end))
            interval_after = (max(s_end, start), end)

            if interval_before[1] > interval_before[0]:
                new_ranges.append(interval_before)
            if interval_contained[1] > interval_contained[0]:
                converted_ranges.append(
                    (
                        interval_contained[0] - s_start + d_start,
                        interval_contained[1] - s_start + d_start,
                    )
                )
            if interval_after[1] > interval_after[0]:
                new_ranges.append(interval_after)

        rng = new_ranges
    return rng + converted_ranges


loc_ranges = []
for start, size in seed_pairs:
    rng = [(start, start + size)]

    for k in maps.keys():
        rng = convert_range(k, rng)

    loc_ranges.append(rng)

loc_ranges_flat = [y for x in loc_ranges for y in x]
min_loc = min([m for m, _ in loc_ranges_flat])
print(min_loc)

part2_time_revised = time() - start_time
print(f"Part 2 time (revised): {part2_time_revised:.5f} s")
print(f"Improvement: {part2_time/part2_time_revised:.2f}x")
