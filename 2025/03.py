data = [l.strip() for l in open('data/3.in')]

def largest_joltage(s: str) -> int:
    j = 0
    for n in range(9, 0, -1):
        if str(n) in s:
            n_idx = s.index(str(n))
            for m in range(9, 0, -1):
                if str(m) in s[n_idx+1:]:
                    if (v:=int(str(n)+str(m))) > j:
                        j = v
                    else:
                        continue
    return j

P1 = sum(largest_joltage(n) for n in data)
print(P1)

max_len = 12

def largest_joltage_recursive(s: str, batteries: str = "") -> int:
    if len(batteries) == max_len:
        return int(batteries)
    
    for n in range(9, 0, -1):
        if str(n) in s:
            n_idx = s.index(str(n))

            if len(s[n_idx+1:]) + len(batteries) + 1 < max_len:
                continue

            return largest_joltage_recursive(s = s[n_idx+1:], batteries=batteries+str(n))

P2 = sum(largest_joltage_recursive(n) for n in data)
print(P2)
