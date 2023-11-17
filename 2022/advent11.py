from functools import reduce
from itertools import groupby
import re
from math import floor

with open("inputs/input11.txt", "r") as f:
    input = f.readlines()

data = [s.strip() for s in input]
monkeys_raw = [list(group) for k, group in groupby(data, lambda x: x == "") if not k]

# Define a Monkey class to handle keeping track of items, interactions, catches and throws
class Monkey:
    def __init__(self, name, items, op, test, test_true, test_false) -> None:
        self.name = name.split(":")[0]
        self.items = [int(n) for n in re.findall("[\d]+", items)]
        self.operation = op.split("=")[-1].strip()
        self.test = int(re.findall("[\d]+", test)[0])
        self.test_true = int(re.findall("[\d]", test_true)[0])
        self.test_false = int(re.findall("[\d]", test_false)[0])
        self.n_inspect = 0

    def take_turn(self):
        items_copy = self.items.copy()
        for i in items_copy:
            new_value = self.inspect(i)
            relief_value = self.worry_relief(new_value)
            if relief_value % self.test == 0:
                self.throw(relief_value, self.test_true)
            else:
                self.throw(relief_value, self.test_false)

    def inspect(self, item):
        old = item
        new = eval(self.operation)
        self.n_inspect += 1
        return new

    def throw(self, item, target):
        self.items.pop(0)
        monkeys[target].catch(item)

    def catch(self, item):
        self.items.append(item)

    def worry_relief(self, w):
        return int(floor(float(w) / 3))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.name}\n\tItems: {self.items}\n\tOperation: {self.operation}\n\tTest: Divible by {self.test}\n\t\tTest true: Throw to {self.test_true}\n\t\tTest false: Throw to {self.test_false}"


# Part 1
monkeys = [Monkey(*m) for m in monkeys_raw]

for i in range(20):
    for m in monkeys:
        m.take_turn()

n_inspections = [m.n_inspect for m in monkeys]
n_inspections.sort()
print(
    "Amount of monkey business after 20 rounds:", n_inspections[-1] * n_inspections[-2]
)

# Part 2
# The worry levels quickly becomes too large to be computationally feasible.
# However, we can utilise the fact that all divisors are coprime and calculate
# the worry-level modulo the lowest common multiple (LCM) to make sure that
# the worry level never increases above LCM. This is a result of The Chinese
# Remainder Theorem. Since our checks are only using remainders, we can use this
# operation which affects all operations equally, without affecting the end
# result.
LCM = reduce(lambda x, y: x * y, [m.test for m in monkeys])


class Monkey2(Monkey):
    def worry_relief(self, w):
        return w % LCM


monkeys = [Monkey2(*m) for m in monkeys_raw]

for i in range(10000):
    for m in monkeys:
        m.take_turn()

n_inspections = [m.n_inspect for m in monkeys]
n_inspections.sort()
n_inspections
print(
    "Amount of monkey business after 10000 rounds:",
    n_inspections[-1] * n_inspections[-2],
)
