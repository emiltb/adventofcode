from itertools import combinations
import matplotlib.pyplot as plt
data = [[int(n) for n in l.strip().split(',')] for l in open('data/9.in')]

def area(a, b):
    return (abs(b[1] - a[1]) + 1) * (abs(b[0] - a[0]) + 1)

P1 = max(area(c1, c2) for c1, c2 in combinations(data, 2))
print(P1)


# lines = list(zip(data, data[1:]))
# print(lines)

# print(min(c[0] for c in data),max(c[0] for c in data))
# print(min(c[1] for c in data),max(c[1] for c in data))

# for r in range(9):
#     for c in range(14):
#         if ([c,r] in data):
#             print('#', end = "")
#         else:
#             print('.', end = "")
#     print()


# for (ac, ar), (bc, br) in combinations(data, 2):
#     print((ac, ar), (bc, br))
#     if ac == bc or ar == br:
#         cc = ac
#         cr = ar
#         dc = bc
#         dr = br

fig = plt.figure()
ax = plt.axes()

# ax.scatter([c[0] for c in data], [c[1] for c in data])

for (ac, ar), (bc, br) in zip(data, data[1:]):
    ax.plot([c[0] for c in data], [c[1] for c in data], marker = 'o', markersize = 0.1)

ax.set_aspect('equal', adjustable='box')
plt.show()