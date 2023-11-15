data = [l.strip() for l in open("data/1.in")]

# Part 1
vals = []
v0 = 0
for v in data:
    if v == "":
        vals.append(v0)
        v0 = 0
    else:
        v0 += int(v)
print(max(vals))

# Part 2
print(sum(sorted(vals)[-3:]))
