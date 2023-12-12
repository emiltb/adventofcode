from ast import literal_eval

data = [
    [a, literal_eval(b)] for a, b in [l.strip().split(" ") for l in open("data/12.in")]
]


def f(string, damaged):
    # print(f"string={string}, damaged={damaged}")
    ans = 0

    if len(damaged) == 0 and "#" in string:
        return 0

    if len(damaged) == 0 and not "#" in string:
        # print("Found a solution!")
        return 1

    if len(string) == 0:
        if damaged:
            return 0
        # print("Found a solution!")
        return 1

    if string[0] == ".":
        ans += f(string[1:], damaged)

    if string[0] == "?":
        for c in ["#", "."]:
            new_string = string.replace("?", c, 1)
            ans += f(new_string, damaged)

    if string[0] == "#":
        len_next_block = damaged[0]
        if len_next_block > len(string):
            return 0
        # print(f"Len of next block: {len_next_block}; Len string: {len(string)}")

        if not "." in string[:len_next_block] and (
            len(string) == len_next_block or string[len_next_block] != "#"
        ):
            new_string = string[len_next_block + 1 :]
            ans += f(new_string, damaged[1:])

    return ans


P1 = 0
for s, d in data:
    ans = f(s, d)
    # print(s, d, ans)
    P1 += ans

print(P1)
