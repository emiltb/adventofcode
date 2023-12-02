import re

data = [l.strip() for l in open("data/2.in")]
games = [l.split(":")[1].split(";") for l in data]


# Part 1
def get_n_colors(s):
    n_colors = tuple()
    for c in ["green", "blue", "red"]:
        n = re.search(f"(\d+) {c}", s)
        n = int(n.group(1)) if n else 0
        n_colors += (n,)

    return n_colors


total = 0
for i, g in enumerate(games):
    max_red = max_green = max_blue = 0
    for draw in g:
        green, blue, red = get_n_colors(draw)
        max_green = max(green, max_green)
        max_blue = max(blue, max_blue)
        max_red = max(red, max_red)

    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        total += i + 1

print(total)

# Part 2
total = 0
for i, g in enumerate(games):
    max_red = max_green = max_blue = 0
    for draw in g:
        green, blue, red = get_n_colors(draw)
        max_green = max(green, max_green)
        max_blue = max(blue, max_blue)
        max_red = max(red, max_red)

    total += max_green * max_blue * max_red

print(total)
