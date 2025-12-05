data = [l.strip() for l in open('data/5.in')]

fresh, ingredients = data[:data.index('')], data[data.index('')+1:]
fresh_intervals = [[int(n1), int(n2)] for n1, n2 in [s.split('-') for s in fresh]]


P1 = 0
for item in ingredients:
    spoiled = 1
    for n1, n2 in fresh_intervals:
        if n1 <= int(item) <= n2:
            spoiled = 0
    
    if spoiled == 0:
        P1 += 1

print(P1)


def merge_ranges(intervals):
    intervals.sort()
    ranges = []
    # Insert the first range
    ranges.append(intervals[0])

    for i in intervals[1:]:
        # If the next range overlaps, modify the endpoint
        if ranges[-1][0] <= i[0] <= ranges[-1][1]:
            ranges[-1][1] = max(ranges[-1][1], i[1])
        else:
            ranges.append(i)

    return ranges

P2 = merge_ranges(fresh_intervals)

print(sum(n2-n1+1 for n1, n2 in P2))