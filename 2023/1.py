import re

data = [l.strip() for l in open("data/1.in")]

# Part 1
digits = [re.findall("\d", s) for s in data]
numbers = [int(n[0]) * 10 + int(n[-1]) for n in digits]
print(sum(numbers))

# Part 2
all_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
all_digits.update({str(v): v for d, v in all_digits.items()})


def get_first_last_digits(s):
    indexes = []
    for d, v in all_digits.items():
        for m in re.finditer(d, s):
            indexes.append((m.start(), v))
    vals = sorted(indexes, key=lambda tup: tup[0])
    return (vals[0][1], vals[-1][1])


digits = [get_first_last_digits(s) for s in data]
numbers = [n[0] * 10 + n[-1] for n in digits]
print(sum(numbers))
