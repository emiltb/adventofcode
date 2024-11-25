# %%
import re
data = [l.strip() for l in open('data/6.in')]


# %% Part 1
grid = [[0] * 1000 for _ in range(1000)]

def perform_action(action, x1, y1, x2, y2):
    for x in range(min(int(x1),int(x2)), max(int(x1),int(x2))+1):
        for y in range(min(int(y1),int(y2)), max(int(y1),int(y2))+1):
            match action:
                case "turn off":
                    grid[x][y] = 0
                case "turn on":
                    grid[x][y] = 1
                case "toggle":
                    grid[x][y] = 0 if grid[x][y] == 1 else 1


for s in data:
    perform_action(*re.findall(r"(turn off|turn on|toggle)\s(\d+),(\d+).*?(\d+),(\d+)", s)[0])

print(sum(y for x in grid for y in x))
    

# %%
grid = [[0] * 1000 for _ in range(1000)]

def perform_action(action, x1, y1, x2, y2):
    for x in range(min(int(x1),int(x2)), max(int(x1),int(x2))+1):
        for y in range(min(int(y1),int(y2)), max(int(y1),int(y2))+1):
            match action:
                case "turn off":
                    grid[x][y] = grid[x][y] - 1 if grid[x][y] > 0 else 0
                case "turn on":
                    grid[x][y] += 1
                case "toggle":
                    grid[x][y] += 2


for s in data:
    perform_action(*re.findall(r"(turn off|turn on|toggle)\s(\d+),(\d+).*?(\d+),(\d+)", s)[0])

print(sum(y for x in grid for y in x))
    
# %%
