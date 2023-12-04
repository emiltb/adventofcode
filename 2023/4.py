# Part 1
data = [[set([int(s) for s in n.split(" ") if s != ""]) for n in l.strip().split(":")[1].split("|")] for l in open("data/4.in")]  # fmt: skip

winning_numbers = [1 * 2 ** (len(s1 & s2) - 1) for s1, s2 in data if len(s1 & s2) > 0]
print(sum(winning_numbers))
