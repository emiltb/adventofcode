from itertools import count

# Part 1
diagonal = count(1)
current_code = 20151125
found_code = False

while found_code == False:
    d = next(diagonal)
    v = list(range(1, d))

    for r, c in zip(reversed(v), v):
        if r == 2947 and c == 3029:
            print(f"({r}, {c}) = {current_code}")
            found_code = True
            break

        current_code = (current_code * 252533) % 33554393
