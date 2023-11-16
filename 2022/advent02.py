import numpy as np

data = np.loadtxt("inputs/input02.txt", dtype="str")

# A, X = ROCK = 1; B, Y = PAPER = 2; C, Z = SCISSORS = 3

# Part 1
def sign_score(b):
    if b == "X":
        return 1
    if b == "Y":
        return 2
    if b == "Z":
        return 3


def game_score(a, b):
    score = sign_score(b)

    # Losing situation
    if (a == "A" and b == "Z") | (a == "B" and b == "X") | (a == "C" and b == "Y"):
        pass
    # Draws
    if (a == "A" and b == "X") | (a == "B" and b == "Y") | (a == "C" and b == "Z"):
        score += 3
    # Wins
    if (a == "A" and b == "Y") | (a == "B" and b == "Z") | (a == "C" and b == "X"):
        score += 6

    return score


total_score = sum([game_score(l[0], l[1]) for l in data])
print("Total score across all games:", total_score)


# Part 2
def game_score_new_rules(a, b):
    score = 0

    # Losing situations: b=X
    if b == "X":
        if a == "A":
            score += sign_score("Z")
        if a == "B":
            score += sign_score("X")
        if a == "C":
            score += sign_score("Y")
    # Draw situations: b=Y
    if b == "Y":
        if a == "A":
            score += sign_score("X")
        if a == "B":
            score += sign_score("Y")
        if a == "C":
            score += sign_score("Z")
        score += 3
    # Winning situations: b=Z
    if b == "Z":
        if a == "A":
            score += sign_score("Y")
        if a == "B":
            score += sign_score("Z")
        if a == "C":
            score += sign_score("X")
        score += 6
    return score


real_total_score = sum([game_score_new_rules(l[0], l[1]) for l in data])
print("Total score across all games:", real_total_score)
