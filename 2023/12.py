from ast import literal_eval

data = [
    [a, literal_eval(b)] for a, b in [l.strip().split(" ") for l in open("data/12.in")]
]

def f(string, damaged, cache):
    key = (string, damaged)
    if key in cache:
        return cache[key]

    ans = 0

    if len(damaged) == 0:
        if "#" in string:
            return 0
        return 1

    if len(string) == 0:
        if damaged:
            return 0
        return 1

    if string[0] == ".":
        ans += f(string[1:], damaged, cache)

    if string[0] == "?":
        for c in ["#", "."]:
            new_string = string.replace("?", c, 1)
            ans += f(new_string, damaged, cache)

    if string[0] == "#":
        len_next_block = damaged[0]
        if len_next_block > len(string):
            return 0

        if not "." in string[:len_next_block] and (
            len(string) == len_next_block or string[len_next_block] != "#"
        ):
            ans += f(string[len_next_block + 1 :], damaged[1:], cache)

    cache[key] = ans
    return ans


# Part 1
P1 = 0
for s, d in data:
    P1 += f(s, d, {})
print(P1)


# Part 2
P2 = 0
for s, d in data:
    s = "?".join([s] * 5)
    d = tuple([x for y in [d] * 5 for x in y])
    P2 += f(s, d, {})
print(P2)
