from functools import cache
data = [int(n) for n in open('data/11.in').read().split()]

for blink in range(25):
    next_row = []
    prev_len = len(data)
    for i, n in enumerate(data):
        str_n = str(n)
        len_n = len(str_n)
        if n == 0:
            next_row += [1]
        elif len_n % 2 == 0:
            p1, p2 = int(str_n[:len_n//2]), int(str_n[len_n//2:])
            next_row += [p1, p2]
        else:
            next_row += [n * 2024]
    data = next_row
print(len(data))


@cache
def count_stones(n, remaining_blinks = 75):
    if remaining_blinks == 0: 
        return 1
    if n == 0: 
        return count_stones(1, remaining_blinks - 1)

    str_n = str(n)
    len_n = len(str_n)
    if len_n % 2 == 0:
        p1 = count_stones(int(str_n[:len_n//2]), remaining_blinks - 1)
        p2 = count_stones(int(str_n[len_n//2:]), remaining_blinks - 1)
        return p1 + p2
    
    return count_stones(n * 2024, remaining_blinks - 1)

data = [int(n) for n in open('data/11.in').read().split()]
print(sum(count_stones(n) for n in data))
