import numpy as np

with open("inputs/input10.txt", "r") as f:
    data = f.readlines()

instructions = [s.strip().split() for s in data]

# Part 1
process = [[1, 1]]
for i in instructions:
    if i[0] == "noop":
        # During a noop only the cycle count increases
        process.append([process[-1][0] + 1, process[-1][1]])
    if i[0] == "addx":
        # During addx the cycle count increases twice and then the result is added
        process.append([process[-1][0] + 1, process[-1][1]])
        process.append([process[-1][0] + 1, process[-1][1] + int(i[1])])

print("Sum of signal strengths:", sum([s[0] * s[1] for s in process[19::40]]))

# Part 2
# Setup a display of zeros
display = np.zeros((6, 40))

# Iterate through each pixel as well as the instructions to draw on the display
for ((y, x), _), (_, s) in zip(np.ndenumerate(display), process):
    if s == x or s == x - 1 or s == x + 1:
        display[y, x] = 1

# Print the display in a compact fashion, to make the text readable
for n in display:
    for d in n:
        if d == 1:
            print("#", sep="", end="")
        else:
            print(" ", sep="", end="")
    print()
