data = [int(l.strip()) for l in open('data/22.in')]

def secret_number(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n

P1 = 0
for n in data:
    for _ in range(2000):
        n = secret_number(n)
    P1 += n
print(P1)
