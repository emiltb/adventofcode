import re


def dfs(blueprint, maxspend, cache, time, bots, amount):
    if time == 0:
        return amount[3]

    key = tuple([time, *bots, *amount])
    if key in cache:
        return cache[key]

    maxval = amount[3] + bots[3] * time
    print(blueprint, time, bots, amount, maxval)

    for bottype, recipe in enumerate(blueprint):
        if bottype != 3 and bots[bottype] >= maxspend[bottype]:
            continue

        wait = 0

        for recipe_amount, recipe_type in recipe:
            if bots[recipe_type] == 0:
                break

            wait = max(
                wait, -(-(recipe_amount - amount[recipe_type]) // bots[recipe_type])
            )
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue

            bots_ = bots[:]
            amt_ = [x + y * (wait + 1) for x, y in zip(amount, bots)]

            for ramt, rtype in recipe:
                amt_[rtype] -= ramt

            bots_[bottype] += 1
            for i in range(3):
                amt_[i] = min(amt_[i], maxspend[i] * remtime)
            maxval = max(maxval, dfs(blueprint, maxspend, cache, remtime, bots_, amt_))

    cache[key] = maxval
    return maxval


data = [l.strip() for l in open("data/19.in")]
total = 0

# Part 1

for i, l in enumerate(data):
    blueprint = []
    maxspend = [0, 0, 0]

    for section in l.split(": ")[1].split(". "):
        recipe = []

        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)

        blueprint.append(recipe)

    print(f"Starting on blueprint {i}")
    v = dfs(blueprint, maxspend, {}, 24, [1, 0, 0, 0], [0, 0, 0, 0])

    print(f"Max for blueprint {i} is {v}")

    total += (i + 1) * v

print(total)

# Part 2
total = 1

for i, l in enumerate(data[:3]):
    blueprint = []
    maxspend = [0, 0, 0]

    for section in l.split(": ")[1].split(". "):
        recipe = []

        for x, y in re.findall(r"(\d+) (\w+)", section):
            x = int(x)
            y = ["ore", "clay", "obsidian"].index(y)
            recipe.append((x, y))
            maxspend[y] = max(maxspend[y], x)

        blueprint.append(recipe)

    v = dfs(blueprint, maxspend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
    total *= v

print(total)
