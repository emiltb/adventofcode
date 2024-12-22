from collections import Counter
data = [int(l.strip()) for l in open('data/22.in')]

def secret_number(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n

secret_numbers = []
P1 = 0
for n in data:
    sn = []
    for _ in range(2000):
        n = secret_number(n)
        sn.append(n % 10)
    P1 += n
    secret_numbers.append(sn)
print(P1)

diffs = []
for s in secret_numbers:
    d = []
    for s1, s2 in zip(s, s[1:]):
        # print(s1, s2, s2 - s1)
        d.append(s2 - s1)
    diffs.append(d)

sequence_candidates = []
for s, d in zip(secret_numbers, diffs):
    for i in range(len(d)):
        if i + 4 < len(s) and s[i + 4] >= 5:
            sequence_candidates.append(tuple(d[i:i+4]))

sequence_candidates = [k for k, _ in Counter(sequence_candidates).most_common(1)]

P2 = {seq: 0 for seq in sequence_candidates}
for test_seq in sequence_candidates:
    for s, d in zip(secret_numbers, diffs):
        for i in range(len(d)):
            if d[i:i+4] == list(test_seq):
                P2[test_seq] += s[i + 4]
                break
print(P2)