with open('inputs/input04.txt', 'r') as f:
    data = f.readlines()

# Remove newlines and split assignments
assignments = [s.strip().split(',') for s in data]
# Separate range endpoints and convert strings to integers
ranges = [[s.split('-') for s in d] for d in assignments]
ranges = [[[int(n) for n in l] for l in s] for s in ranges]

# Part 1
def contains(a,b):
    # Returns true if b is contained in a
    return (a[0] <= b[0]) and (a[1] >= b[1])

assignments_contains = [contains(a,b) or contains(b,a) for (a,b) in ranges]

print('Number of assigments contained in another:', sum(assignments_contains))

# Part 2
def overlaps(a,b):
    # Returns true if a and b overlaps
    return max([a[0],b[0]]) <= min([a[1],b[1]])

assignments_overlaps = [overlaps(a,b) for (a,b) in ranges]

print('Number of assigments overlapping eachother:', sum(assignments_overlaps))
