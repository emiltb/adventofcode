import numpy as np
from functools import reduce

with open("inputs/input08.txt", "r") as f:
    raw_data = f.readlines()

# Read the data into a numpy array
data = np.array([[c for c in s.strip()] for s in raw_data]).astype(int)
len_y, len_x = data.shape

# Part 1
# From each tree find the vector of tree that extend in all four directions
# If all the trees in a direction a smaller than the current tree, it can be
# seen from the outside.
# We only need it accessible from one of the four directions.
n_visible = 0
for (x, y), h in np.ndenumerate(data):
    if (x == 0) or (y == 0) or (x == len_x - 1) or (y == len_y - 1):
        # We are at an edge
        n_visible += 1
    else:
        left = np.all(h > data[x, :y])  # Left
        right = np.all(h > data[x, (y + 1) :])  # right
        above = np.all(h > data[:x, y])  # Above
        below = np.all(h > data[(x + 1) :, y])  # Below

        if np.any([left, right, above, below]):
            n_visible += 1

print("Number of visible trees:", n_visible)


# Part 2
# Function that iterates over a vector of trees and counts the number of
# trees that can be seen
def count_trees(vec):
    trees = 0
    for n in vec:
        if n == True:
            trees += 1
        elif n == False:
            trees += 1
            break
    return trees


# Iterate over all trees and calculate the scenic score for each
# Vectors are found in a similar fashion to above, but left and above
# are flipped, as the order of elements is important here.
scenic_score = np.zeros(data.shape)
for (x, y), h in np.ndenumerate(data):
    left = np.flip(h > data[x, :y])  # Left
    right = h > data[x, (y + 1) :]  # Right
    above = np.flip(h > data[:x, y])  # Above
    below = h > data[(x + 1) :, y]  # Below

    scores = [count_trees(v) for v in [left, right, above, below]]

    scenic_score[x, y] = reduce(lambda x, y: x * y, scores)

print("Maximum scenic score in forest:", scenic_score.max())
