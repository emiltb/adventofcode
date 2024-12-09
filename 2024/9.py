from tqdm import tqdm
data = open('data/9.in').read().strip()

mem = []
fid = 0
for i, s in enumerate(data):
    if i % 2 == 0:
        mem += [fid] * int(s)
        fid += 1
    else:
        mem += [None] * int(s)

for i in tqdm(range(len(mem))):
    if not None in mem: break
    v = mem.pop()
    if v: mem[mem.index(None)] = v

print(sum(i*v for i, v in enumerate(mem) if v is not None))

t = lambda n: n // 2 if n % 2 == 0 else None

mem = [(t(i), int(n)) for i, n in enumerate(data)]
moved = set()

for i in tqdm(range(len(mem))):
    fid, fsize = mem[-i-1]
    if fid and fid not in moved:
        fidx = -i-1 + len(mem)
        moved.add(fid)
        for pid, psize in ((j,l) for j, (v, l) in enumerate(mem) if v is None):
            if psize >= fsize and fidx > pid:
                mem[pid] = mem[-i-1]
                if psize == fsize:
                    mem[-i-1] = (None, psize)
                else: 
                    mem[-i-1] = (None, fsize)
                    mem.insert(pid+1, (None, psize - fsize))
                break

res = []
for v, l in mem:
    res += [v]*l

print(sum(i*v for i, v in enumerate(res) if v is not None))