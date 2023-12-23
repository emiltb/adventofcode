from collections import defaultdict
from itertools import chain

data = [
    [[int(n) for n in s.split(",")] for s in l.strip().split("~")]
    for l in open("data/22.in")
]
data.sort(key=lambda x: x[0][2])

# Part 1
bricks = dict()
for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(data):
    brick = []
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                brick.append([x, y, z])
    bricks[i] = brick


new_stack = dict()
for key, brick in bricks.items():
    if any(z == 1 for _, _, z in brick):
        new_stack[key] = brick
        continue

    while True:
        new_block = [[x, y, z - 1] for x, y, z in brick]
        if any(e in chain(*new_stack.values()) for e in new_block) or any(
            z == 0 for _, _, z in new_block
        ):
            break
        brick = new_block
    new_stack[key] = brick


supported_by = defaultdict(set)
for i, block in new_stack.items():
    for b in [[x, y, z - 1] for x, y, z in block]:
        supported_by[i] = supported_by[i] | {
            k for k, v in new_stack.items() if b in v and k != i
        }

# Bricks not supporting any bricks
bricks_not_supporting = set(new_stack.keys()) - set().union(*supported_by.values())
bricks_support_more_than_one = set().union(
    *[v for k, v in supported_by.items() if len(v) > 1]
)
bricks_as_only_support = set().union(
    *[v for k, v in supported_by.items() if len(v) == 1]
)

P1 = len(bricks_not_supporting | bricks_support_more_than_one - bricks_as_only_support)
print(P1)

# Part 2
disintegrate_candicates = set(new_stack.keys()) - (
    bricks_not_supporting | bricks_support_more_than_one - bricks_as_only_support
)

P2 = 0
for d in disintegrate_candicates:
    falling_bricks = set()
    test_stack = dict(new_stack)
    test_stack.pop(d, None)

    new_test_stack = dict()
    for key, brick in test_stack.items():
        if any(z == 1 for _, _, z in brick):
            new_test_stack[key] = brick
            continue

        while True:
            new_block = [[x, y, z - 1] for x, y, z in brick]
            if any(e in chain(*new_test_stack.values()) for e in new_block) or any(
                z == 0 for _, _, z in new_block
            ):
                break
            brick = new_block
            falling_bricks.add(key)
        new_test_stack[key] = brick
    P2 += len(falling_bricks)

print(P2)
