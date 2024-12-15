from collections import deque
grid, instructions = open('data/15.in').read().split('\n\n')
grid = grid.split()
rows = len(grid)
cols = len(grid[0])

grid = {(r,c): s for r, l in enumerate(grid) for c, s in enumerate(l)}
instructions = deque("".join(instructions.split()))
dirs = {'^': (-1,0), 'v': (1,0), '>': (0,1), '<': (0,-1)}
pos = [(r,c) for (r,c), s in grid.items() if s == "@"][0]

def print_grid():
    for r in range(rows):
        for c in range(cols):
            print(grid[(r,c)], end = '')
        print()
    print()

def push(r, c, dr, dc):
    next_pos = (r + dr, c + dc)
    if grid[next_pos] == 'O':
        push(*next_pos, dr, dc)
    if grid[next_pos] == '.':
        grid[next_pos] = 'O'
        grid[(r,c)] = '.'

while instructions:
    dr, dc = dirs[instructions.popleft()]
    r, c = pos
    next_pos = (r + dr, c + dc)

    if grid[next_pos] == 'O':
        push(*next_pos, dr, dc)

    if grid[next_pos] == '.':
        grid[next_pos] = '@'
        grid[pos] = '.'
        pos = next_pos

print(sum(r * 100 + c for (r, c), s in grid.items() if s == 'O'))




# grid, instructions = open('data/15.test.in').read().split('\n\n')
# grid = grid.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.').split()
# rows = len(grid)
# cols = len(grid[0])
# grid = {(r,c): s for r, l in enumerate(grid) for c, s in enumerate(l)}
# instructions = deque("".join(instructions.split()))

# def can_move(r, c, dr, dc):
#     print(f"can_move({r},{c},{dr},{dc})")
#     next_pos = (r + dr, c + dc)

#     print(f"\tCurrent position: {(r,c)}, {grid[(r,c)]}")
#     print(f"\tNext position: {(next_pos)}, {grid[next_pos]}")

#     if grid[next_pos] == ']':
#         return can_move(*next_pos, dr, dc) and can_move(r + dr, c - 1, dr, dc)
    
#     if grid[next_pos] == '[':
#         return can_move(*next_pos, dr, dc) and can_move(r + dr, c + 1, dr, dc)
    
#     if grid[next_pos] == '.':
#         print("Box can be moved")
#         return True

#     return False

# print_grid()


# def push_big(r, c, dr, dc):
#     next_pos = (r + dr, c + dc)
#     if dr == 0:
#         if grid[next_pos] in '[]':
#             push_big(*next_pos, dr, dc)
#         if grid[next_pos] == '.':
#             grid[next_pos] = grid[(r,c)]
#             grid[(r,c)] = '.'
#     if dr != 0:
#         # print('Try to push big box vertical')
#         # print('Next pos', grid[next_pos])

#         dc2 = 1 if grid[(r,c)] == '[' else -1
#         if can_move(*next_pos, dr, dc):
#             push_big(r + dr, c + dc2, dr, dc)
#             push_big(*next_pos, dr, dc)

#         if grid[next_pos] == '.' and grid[(r + dr, c + dc2)] == '.':
#             # print("Big box can be pushed")
#             grid[next_pos] = grid[(r,c)]
#             grid[(r + dr, c + dc2)] = grid[(r,c + dc2)]
#             grid[(r,c)] = '.'
#             grid[(r,c + dc2)] = '.'

# pos = [(r,c) for (r,c), s in grid.items() if s == "@"][0]
# print_grid()
# while instructions:
#     ins = instructions.popleft()
#     print(f"Move {ins}:")
#     dr, dc = dirs[ins]
#     r, c = pos
#     next_pos = (r + dr, c + dc)
#     # print(r, c, dr, dc, next_pos)

#     if grid[next_pos] in '[]':
#         # print("Try to push")
#         push_big(*next_pos, dr, dc)

#     if grid[next_pos] == '.':
#         # print(dr, dc, 'moving')
#         grid[next_pos] = '@'
#         grid[pos] = '.'
#         pos = next_pos
#     print_grid()

        
#     # print(dr, dc, pos)

# print(sum(r * 100 + c for (r, c), s in grid.items() if s == '['))

# print([(r,c) for (r,c), s in grid.items() if s == "@"][0])
# print(can_move(5,7,-1,0))

# # for k, v in grid.items():
# #     print(k, v)